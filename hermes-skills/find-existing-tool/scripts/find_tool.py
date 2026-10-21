#!/usr/bin/env python3
"""HVE wrapper around the vendored awesome-reverse-engineered index search.

Search never touches the network: it reads only the validated local copy of
entries.json. Only `refresh` (and `info --readme` / `clone --confirm`) go online,
and none of them ever send a GitHub credential.

Commands:
  find_tool.py refresh [--if-stale HOURS] [--from-file PATH] [--url URL] [--min-entries N]
  find_tool.py search <words...> [--category T] [--lang L] [--min-stars N]
                     [--include-archived] [--show-risky] [--limit N] [--json]
  find_tool.py info <owner/repo|url> [--readme] [--lines N] [--json]
  find_tool.py clone <owner/repo|url> --confirm [--dest DIR] [--allow-in-repo]
  find_tool.py status [--json]
  find_tool.py categories

Cache (outside the repo): $HVE_RE_INDEX_HOME, else $XDG_CACHE_HOME/hve/find-existing-tool,
else ~/.cache/hve/find-existing-tool. Files: entries.json (current good),
entries.prev.json (previous good), meta.json.
Python standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

sys.dont_write_bytecode = True  # never leave __pycache__ in the skill (or repo) directory

# --- Credential isolation: drop every GitHub token before anything else runs. ---
for _var in ("GITHUB_TOKEN", "GH_TOKEN", "GH_ENTERPRISE_TOKEN", "GITHUB_ENTERPRISE_TOKEN"):
    os.environ.pop(_var, None)

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
VENDORED = HERE / "vendor" / "re_index.py"
VENDORED_SHA256 = "5cad537f25fde5a094888e11e1c89d24ae5f17c81564c4ef784460ca2131234b"
UPSTREAM_COMMIT = "586cffd011070efff6875b3f3921b05637f67786"
DATA_URL = "https://raw.githubusercontent.com/alexgaoth/awesome-reverse-engineered/main/data/entries.json"
MIN_ENTRIES = 10000          # upstream had 12,866 on 2026-10-21
MAX_SHRINK = 0.80            # reject a refresh that drops below 80% of last-good count
STALE_WARN_H = 48
REQUIRED_KEYS = ("name", "url", "category")

# Deprioritised in hermes/knowledge/2026-10-21-re-priorities.md: hidden unless --show-risky.
SUPPRESSED_FLAGS = {"TOS_LLM_WEB_API", "TOS_SUBSCRIPTION_PROXY", "LEAKED_CONTENT"}

FLAG_TEXT = {
    "TOS_LLM_WEB_API": "wraps a commercial LLM web app as an API; likely violates provider ToS; routes data to cloud",
    "TOS_SUBSCRIPTION_PROXY": "reuses a paid subscription/OAuth session as an API; likely violates provider ToS",
    "LEAKED_CONTENT": "leaked/extracted vendor prompts or source; unclear IP and provenance",
    "TOS_UNOFFICIAL_CLIENT": "unofficial client of a third-party service; may breach ToS or lock the account; own accounts only",
    "SCRAPING": "crawler/downloader; respect ToS, rate limits and copyright; no mass scraping",
    "CREDENTIAL_HANDLING": "handles tokens, cookies or session credentials; read the code before giving it any secret",
    "TOS_PRIVATE_SERVER": "private/revival server for a commercial game or service; check ToS",
    "LICENSE_NONE": "no license detected: all rights reserved by default",
    "LICENSE_COPYLEFT": "copyleft license; affects redistribution of derived work",
    "LICENSE_UNCLEAR": "license not identified (NOASSERTION/other); read the repo before reuse",
}

EXTRA_SYNONYMS = {
    "llm": ["language model"], "llms": ["llm", "language model"], "ai": ["llm", "machine learning"],
    "re": ["reverse engineer"], "iot": ["smart home"], "nvidia": ["cuda", "geforce", "jetson"],
    "gpu": ["graphics"], "mcp": ["model context protocol"], "firmware": ["bootloader"],
}


# ---------------------------------------------------------------------------
# Vendored module
# ---------------------------------------------------------------------------
def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_vendored():
    actual = _sha256(VENDORED)
    if actual != VENDORED_SHA256:
        print(f"warning: vendored re_index.py sha256 {actual[:12]}… does not match pinned "
              f"{VENDORED_SHA256[:12]}…; see scripts/vendor/VENDORED.md", file=sys.stderr)
    spec = importlib.util.spec_from_file_location("re_index_vendored", VENDORED)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # module has no import-time side effects (main() is guarded)
    return mod


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------
def cache_dir() -> Path:
    if os.environ.get("HVE_RE_INDEX_HOME"):
        d = Path(os.environ["HVE_RE_INDEX_HOME"]).expanduser()
    else:
        base = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
        d = base / "hve" / "find-existing-tool"
    d = d.resolve()
    if d == SKILL_DIR or SKILL_DIR in d.parents:
        sys.exit(f"error: cache dir {d} is inside the skill directory; index data must stay out of the repo")
    return d


def paths():
    d = cache_dir()
    return d, d / "entries.json", d / "entries.prev.json", d / "meta.json"


def read_meta() -> dict:
    _, _, _, meta = paths()
    try:
        return json.loads(meta.read_text())
    except Exception:
        return {}


def validate(raw: bytes, min_entries: int, last_count: int | None) -> list:
    try:
        data = json.loads(raw)
    except Exception as ex:
        raise ValueError(f"not valid JSON: {ex}")
    if not isinstance(data, list):
        raise ValueError("top level is not a list")
    if len(data) < min_entries:
        raise ValueError(f"only {len(data)} entries (< min {min_entries})")
    if last_count and len(data) < MAX_SHRINK * last_count:
        raise ValueError(f"{len(data)} entries is a >{int((1 - MAX_SHRINK) * 100)}% drop from last-good {last_count}")
    bad = sum(1 for e in data if not isinstance(e, dict) or any(not e.get(k) for k in REQUIRED_KEYS))
    if bad > 0.01 * len(data):
        raise ValueError(f"{bad} entries missing {REQUIRED_KEYS}")
    return data


def cmd_refresh(a) -> int:
    d, cur, prev, meta = paths()
    d.mkdir(parents=True, exist_ok=True)
    m = read_meta()
    if a.if_stale is not None and cur.exists():
        age_h = (time.time() - cur.stat().st_mtime) / 3600
        if age_h < a.if_stale:
            print(f"fresh: {age_h:.1f} h old (< {a.if_stale} h); no refresh")
            return 0
    source = a.from_file or a.url
    try:
        if a.from_file:
            raw = Path(a.from_file).read_bytes()
        else:
            req = urllib.request.Request(a.url, headers={"User-Agent": "hve-find-existing-tool/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:  # no Authorization header, ever
                raw = r.read()
        data = validate(raw, a.min_entries, m.get("count"))
    except Exception as ex:
        print(f"refresh FAILED ({source}): {ex}", file=sys.stderr)
        if cur.exists():
            print(f"kept last-good copy: {m.get('count', '?')} entries fetched {m.get('fetched_at', '?')}",
                  file=sys.stderr)
        return 2
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".entries.", suffix=".tmp")
    with os.fdopen(fd, "wb") as f:
        f.write(raw)
    if cur.exists():
        shutil.copy2(cur, prev)
        if meta.exists():
            shutil.copy2(meta, d / "meta.prev.json")
    os.replace(tmp, cur)
    new_meta = {
        "fetched_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": source, "count": len(data), "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw), "vendored_upstream_commit": UPSTREAM_COMMIT,
    }
    meta.write_text(json.dumps(new_meta, indent=1))
    print(f"refreshed: {len(data)} entries, {len(raw):,} bytes, sha256 {new_meta['sha256'][:12]}… -> {cur}")
    return 0


def load_entries() -> tuple[list, dict]:
    _, cur, prev, _ = paths()
    for p in (cur, prev):
        if p.exists():
            try:
                return json.loads(p.read_text()), read_meta() if p == cur else {"fetched_at": "?", "note": "using entries.prev.json"}
            except Exception as ex:
                print(f"warning: {p} unreadable ({ex}); trying fallback", file=sys.stderr)
    sys.exit("error: no local index. Run: find_tool.py refresh   (or refresh --from-file <entries.json> offline)")


# ---------------------------------------------------------------------------
# Query expansion and scoring
# ---------------------------------------------------------------------------
def variants(term: str, upstream_syn: dict) -> list[tuple[str, float, bool]]:
    """Return (text, weight_factor, match_mode) alternatives for one user term."""
    out = [(term, 1.0, "prefix" if len(term) <= 3 else "substr")]
    alts = set(upstream_syn.get(term, [])) | set(EXTRA_SYNONYMS.get(term, []))
    if len(term) > 3:
        if term.endswith("ies"):
            alts.add(term[:-3] + "y")
        elif term.endswith("es") and len(term) > 4:
            alts.update({term[:-2], term[:-1]})
        elif term.endswith("s") and not term.endswith("ss"):
            alts.add(term[:-1])
    out += [(x, 0.7, "word" if len(x) <= 3 else "substr") for x in sorted(alts) if x != term]
    return out


def hit(text_alt: str, mode: str, text: str) -> bool:
    """substr: plain substring (long terms). prefix: user's short term must start a word but may
    continue (llm -> llms, llm4decompile, llm-based). word: short synonym must be a whole word."""
    if mode == "prefix":
        return re.search(rf"(?<![a-z0-9]){re.escape(text_alt)}", text) is not None
    if mode == "word":
        return re.search(rf"(?<![a-z0-9]){re.escape(text_alt)}(?![a-z0-9])", text) is not None
    return text_alt in text


def score(e: dict, groups: list, fields_fn) -> tuple[int, float] | None:
    fs = fields_fn(e)
    matched, total = 0, 0.0
    for alts in groups:
        best = 0.0
        for alt, factor, mode in alts:
            for w, text in fs:
                if hit(alt, mode, text):
                    best = max(best, w * factor)
        if best:
            matched += 1
            total += best
    if not matched:
        return None
    total += 0.8 * math.log10((e.get("stars") or 0) + 1)
    if e.get("archived"):
        total -= 1.0
    if health(e)[0] == "dormant":
        total -= 0.5
    return matched, total


def health(e: dict) -> tuple[str, str]:
    if e.get("archived"):
        return "archived", "🗄️"
    p = e.get("pushed")
    if not p:
        return "unknown", "⚪"
    try:
        age = (dt.date.today() - dt.date.fromisoformat(p[:10])).days
    except ValueError:
        return "unknown", "⚪"
    if age <= 365:
        return "active", "🟢"
    if age <= 3 * 365:
        return "slowing", "🟡"
    return "dormant", "🔴"


def flags(e: dict) -> list[str]:
    cat, sub = e.get("category", ""), e.get("subcategory", "") or ""
    desc = (e.get("desc", "") + " " + e.get("name", "") + " " + " ".join(e.get("topics") or [])).lower()
    f = []
    if sub in ("Chatbot Web APIs", "Chinese LLM Web APIs"):
        f.append("TOS_LLM_WEB_API")
    if sub.startswith("Coding Agents") and re.search(
            r"proxy|compatible|subscription|oauth|2api|gateway|relay|reverse[- ]engineered .*api|free", desc):
        f.append("TOS_SUBSCRIPTION_PROXY")
    if sub == "System Prompt Leaks & Extractions" or re.search(r"\bleak", desc):
        f.append("LEAKED_CONTENT")
    if (cat in ("Unofficial Web/App API Clients", "Messaging & Social Apps", "Chinese & Asian Platforms",
                "Third-party Clients", "Alternative Frontends", "Mobile Apps")
            or sub == "MCP Servers for Private APIs"):
        f.append("TOS_UNOFFICIAL_CLIENT")
    if re.search(r"crawler|scrap|bulk[- ]download|batch download|downloader", desc):
        f.append("SCRAPING")
    if re.search(r"token|cookie|session|credential|password|login", desc):
        f.append("CREDENTIAL_HANDLING")
    if sub == "Private Servers":
        f.append("TOS_PRIVATE_SERVER")
    lic = (e.get("license") or "").upper()
    if not lic:
        f.append("LICENSE_NONE")
    elif "GPL" in lic:
        f.append("LICENSE_COPYLEFT")
    elif lic in ("NOASSERTION", "OTHER"):
        f.append("LICENSE_UNCLEAR")
    return f


def enrich(e: dict) -> dict:
    h, icon = health(e)
    fl = flags(e)
    return {
        "name": e.get("name"), "url": e.get("url"), "desc": e.get("desc", ""),
        "category": e.get("category"), "subcategory": e.get("subcategory"),
        "license": e.get("license") or None, "stars": e.get("stars"), "pushed": e.get("pushed"),
        "archived": bool(e.get("archived")), "lang": e.get("lang") or None,
        "health": h, "health_icon": icon, "flags": fl,
        "suppressed_by_default": bool(SUPPRESSED_FLAGS & set(fl)),
    }


def fmt(i: int, r: dict) -> str:
    where = r["category"] + (f" › {r['subcategory']}" if r.get("subcategory") else "")
    stars = f"★{r['stars']:,}" if r.get("stars") is not None else "★?"
    lic = r["license"] or "NONE (all rights reserved)"
    lines = [f"{i}. {r['name']} — {r['url']}",
             f"   {r['desc']}  [{where}]",
             f"   health: {r['health_icon']} {r['health']} · {stars} · pushed {r['pushed'] or '?'}"
             f" · {r['lang'] or '?'} · license {lic}"]
    if r["flags"]:
        lines.append("   flags: " + "; ".join(f"{x} ({FLAG_TEXT[x]})" for x in r["flags"]))
    else:
        lines.append("   flags: none")
    return "\n".join(lines)


def header(entries: list, meta: dict) -> str:
    fetched = meta.get("fetched_at", "?")
    age = ""
    try:
        t = dt.datetime.strptime(fetched, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        hours = (dt.datetime.now(dt.timezone.utc) - t).total_seconds() / 3600
        age = f", age {hours:.1f} h" + (" (STALE: run refresh)" if hours > STALE_WARN_H else "")
    except ValueError:
        pass
    return f"index: {len(entries):,} entries, fetched {fetched}{age}"


def cmd_search(a, mod) -> int:
    entries, meta = load_entries()
    syn = getattr(mod, "SYNONYMS", {})
    terms = [t for t in re.split(r"[\s,]+", " ".join(a.words).lower()) if t]
    groups = [variants(t, syn) for t in terms]
    res, hidden = [], 0
    for e in entries:
        if a.category and a.category.lower() not in (e.get("category", "") + " " + (e.get("subcategory") or "")).lower():
            continue
        if a.lang and (e.get("lang") or "").lower() != a.lang.lower():
            continue
        if (e.get("stars") or 0) < a.min_stars or (e.get("archived") and not a.include_archived):
            continue
        sc = score(e, groups, mod.fields)
        if not sc:
            continue
        r = enrich(e)
        if r["suppressed_by_default"] and not a.show_risky:
            hidden += 1
            continue
        res.append((sc, r))
    res.sort(key=lambda x: (-x[0][0], -x[0][1]))
    full = [r for (m, _), r in res if m == len(terms)]
    partial = [r for (m, _), r in res if m < len(terms)]
    out = (full + partial)[: a.limit]
    expanded = [" | ".join(alt + ("*" if mode == "prefix" else "") for alt, _, mode in g) for g in groups]
    if a.json:
        print(json.dumps({"query": terms, "expanded": expanded, "index": meta, "total_matches": len(res),
                          "full_matches": len(full), "hidden_risky": hidden, "results": out},
                         indent=1, ensure_ascii=False))
        return 0
    print(f'query: "{" ".join(terms)}" · expanded: ' + " + ".join(f"({x})" for x in expanded))
    print(header(entries, meta) + f" · {len(res)} matches ({len(full)} match all terms)\n")
    if not out:
        print("No matches. Try fewer or broader words, the vendor name, or `categories`.")
    elif not full:
        print("(no project matches all terms; showing partial matches)\n")
    for n, r in enumerate(out, 1):
        print(fmt(n, r) + "\n")
    if hidden:
        print(f"{hidden} deprioritised result(s) hidden ({', '.join(sorted(SUPPRESSED_FLAGS))}); "
              "rerun with --show-risky only if Hans explicitly needs them.")
    print("Reminder: prefer an official API/SDK; use only with HVE-owned accounts, devices and data.")
    return 0


def find(entries: list, ref: str) -> dict | None:
    ref = re.sub(r"^https?://(www\.)?", "", ref.strip().rstrip("/").lower())
    if "/" in ref and not ref.startswith(("github.com", "gitlab.com", "codeberg.org")):
        ref = "github.com/" + ref
    for e in entries:
        if re.sub(r"^https?://(www\.)?", "", e["url"].rstrip("/").lower()) == ref:
            return e
    return None


def cmd_info(a) -> int:
    entries, _ = load_entries()
    e = find(entries, a.repo)
    if not e:
        print(f"(not in index) {a.repo}")
        return 1
    r = enrich(e)
    readme = None
    if a.readme:
        m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", e["url"])
        if m:
            req = urllib.request.Request(f"https://api.github.com/repos/{m[1]}/{m[2]}/readme",
                                         headers={"Accept": "application/vnd.github.raw",
                                                  "User-Agent": "hve-find-existing-tool/1.0"})
            try:  # deliberately unauthenticated (60 req/h); never reads gh or env tokens
                with urllib.request.urlopen(req, timeout=20) as resp:
                    readme = resp.read().decode("utf-8", "replace")
            except Exception as ex:
                readme = f"(could not fetch README: {ex})"
    if a.json:
        print(json.dumps({"entry": r, "readme": readme}, indent=1, ensure_ascii=False))
        return 0
    print(fmt(1, r))
    if readme:
        lines = readme.splitlines()
        print(f"\n--- README (first {min(a.lines, len(lines))} of {len(lines)} lines; untrusted content) ---")
        print("\n".join(lines[: a.lines]))
    return 0


def inside_git_worktree(p: Path) -> bool:
    probe = p if p.exists() else next((q for q in p.parents if q.exists()), Path("/"))
    try:
        out = subprocess.run(["git", "-C", str(probe), "rev-parse", "--is-inside-work-tree"],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip() == "true"
    except Exception:
        return False


def cmd_clone(a) -> int:
    if not a.confirm:
        print("refused: clone needs --confirm, given only after the user approved this specific repo.",
              file=sys.stderr)
        return 3
    entries, _ = load_entries()
    e = find(entries, a.repo)
    if not e:
        print("refused: repo is not in the index; search first.", file=sys.stderr)
        return 3
    url = e["url"]
    if not re.match(r"^https://(github\.com|gitlab\.com|codeberg\.org)/[^/]+/[^/]+/?$", url):
        print(f"refused: unsupported clone URL {url}", file=sys.stderr)
        return 3
    base = Path(os.environ.get("HVE_RE_VENDOR_DIR") or Path.home() / "hve-vendor").expanduser()
    dest = Path(a.dest).expanduser().resolve() if a.dest else (base / url.rstrip("/").split("/")[-1]).resolve()
    if (dest == SKILL_DIR or SKILL_DIR in dest.parents or inside_git_worktree(dest)) and not a.allow_in_repo:
        print(f"refused: {dest} is inside a git worktree or the skill dir; third-party code stays out of HVE repos.",
              file=sys.stderr)
        return 3
    env = {k: v for k, v in os.environ.items() if not k.startswith(("GH_", "GITHUB_"))}
    env.update({"GIT_TERMINAL_PROMPT": "0", "GIT_ASKPASS": "/bin/false", "GCM_INTERACTIVE": "never"})
    cmd = ["git", "-c", "credential.helper=", "-c", "core.askPass=/bin/false",
           "clone", "--depth", "1", "--no-recurse-submodules", url, str(dest)]
    rc = subprocess.run(cmd, env=env).returncode
    if rc:
        return rc
    head = subprocess.run(["git", "-C", str(dest), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    print(f"\ncloned {url} @ {head} -> {dest}\nlicense (index): {e.get('license') or 'NONE (all rights reserved)'}\n"
          "Treat as untrusted: read before running; never pass credentials to it unreviewed.")
    return 0


def cmd_status(a) -> int:
    d, cur, prev, _ = paths()
    st = {"cache_dir": str(d), "entries": cur.exists(), "prev": prev.exists(), "meta": read_meta(),
          "vendored_sha256_ok": _sha256(VENDORED) == VENDORED_SHA256, "upstream_commit": UPSTREAM_COMMIT}
    if cur.exists():
        st["age_hours"] = round((time.time() - cur.stat().st_mtime) / 3600, 2)
    print(json.dumps(st, indent=1) if a.json else "\n".join(f"{k}: {v}" for k, v in st.items()))
    return 0 if cur.exists() else 1


def cmd_categories() -> int:
    entries, _ = load_entries()
    counts: dict = {}
    for e in entries:
        counts.setdefault(e["category"], {}).setdefault(e.get("subcategory", ""), 0)
        counts[e["category"]][e.get("subcategory", "")] += 1
    for cat in sorted(counts):
        print(f"{cat} ({sum(counts[cat].values())})")
        for sc, n in sorted(counts[cat].items(), key=lambda x: -x[1]):
            print(f"  - {sc} ({n})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("refresh")
    r.add_argument("--if-stale", type=float, metavar="HOURS")
    r.add_argument("--from-file")
    r.add_argument("--url", default=DATA_URL)
    r.add_argument("--min-entries", type=int, default=MIN_ENTRIES)
    s = sub.add_parser("search")
    s.add_argument("words", nargs="+")
    s.add_argument("--category"); s.add_argument("--lang")
    s.add_argument("--min-stars", type=int, default=0)
    s.add_argument("--include-archived", action="store_true")
    s.add_argument("--show-risky", action="store_true")
    s.add_argument("--limit", type=int, default=8)
    s.add_argument("--json", action="store_true")
    i = sub.add_parser("info")
    i.add_argument("repo"); i.add_argument("--readme", action="store_true")
    i.add_argument("--lines", type=int, default=60); i.add_argument("--json", action="store_true")
    c = sub.add_parser("clone")
    c.add_argument("repo"); c.add_argument("--dest")
    c.add_argument("--confirm", action="store_true"); c.add_argument("--allow-in-repo", action="store_true")
    t = sub.add_parser("status"); t.add_argument("--json", action="store_true")
    sub.add_parser("categories")
    a = ap.parse_args()
    if a.cmd == "refresh":
        return cmd_refresh(a)
    if a.cmd == "search":
        return cmd_search(a, load_vendored())
    if a.cmd == "info":
        return cmd_info(a)
    if a.cmd == "clone":
        return cmd_clone(a)
    if a.cmd == "status":
        return cmd_status(a)
    return cmd_categories()


if __name__ == "__main__":
    raise SystemExit(main())
