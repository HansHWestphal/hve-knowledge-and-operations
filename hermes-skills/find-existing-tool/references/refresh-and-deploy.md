# Refresh and deployment (find-existing-tool)

Status: proposal. Nothing here has been checked on the DGX Spark Hermes host.
Verify the live host, profile and scheduler before enabling it.

## Layout on the host
- Skill files: copy or sync `hermes-skills/find-existing-tool/` into the Hermes profile's skills directory, the same way existing HVE skills are mirrored. Earlier evidence for `x-333-quote` shows `~/.hermes/profiles/<profile>/skills/hve/<skill>/`.
- Index cache (never in a repo): `$HVE_RE_INDEX_HOME`, default `~/.cache/hve/find-existing-tool/`.
  - `entries.json`: current validated copy (~5.6 MB, ~12.9k entries on 2026-10-21)
  - `entries.prev.json`, `meta.prev.json`: previous good copy
  - `meta.json`: fetched_at, source, count, sha256, bytes
- Optional clone target: `$HVE_RE_VENDOR_DIR`, default `~/hve-vendor/`. It must not be inside a git worktree.

## First run / offline seeding
```bash
python3 scripts/find_tool.py refresh                         # online
python3 scripts/find_tool.py refresh --from-file entries.json  # offline seed from a copied file
python3 scripts/find_tool.py status
```

## Daily refresh: pick one scheduler

Hermes cron (preferred if the profile already runs cron jobs): a daily job that runs
```bash
python3 <skill>/scripts/find_tool.py refresh --if-stale 20
```
and reports a non-zero exit code (2 = validation or download failed; the last-good copy is kept).

systemd user timer:
```ini
# ~/.config/systemd/user/hve-find-tool-refresh.service
[Service]
Type=oneshot
ExecStart=/usr/bin/python3 %h/.hermes/profiles/<profile>/skills/hve/find-existing-tool/scripts/find_tool.py refresh --if-stale 20

# ~/.config/systemd/user/hve-find-tool-refresh.timer
[Timer]
OnCalendar=*-*-* 13:00:00 UTC
Persistent=true
RandomizedDelaySec=15m
[Install]
WantedBy=timers.target
```
`systemctl --user enable --now hve-find-tool-refresh.timer`. Upstream's nightly data refresh lands around 12:05 UTC (observed 2026-10-21), so 13:00 UTC picks it up.

crontab fallback: `0 13 * * * python3 <skill>/scripts/find_tool.py refresh --if-stale 20 >> ~/.cache/hve/find-existing-tool/refresh.log 2>&1`

## Validation rules applied on every refresh
- Parses as JSON, top level is a list.
- At least 10,000 entries (`--min-entries` overrides this).
- No more than a 20% drop compared with the last-good count.
- Fewer than 1% of entries missing `name`, `url` or `category`.
- Atomic replace. The previous good copy is kept as `entries.prev.json`.
- If `entries.json` becomes unreadable, search falls back to `entries.prev.json`.

## Network and credentials
- Only `refresh`, `info --readme` and `clone --confirm` use the network.
- No Authorization header is ever sent.
- `GITHUB_TOKEN`, `GH_TOKEN` and the enterprise variants are removed from the process environment at startup.
- `gh` is never called.
- `clone` runs git with an empty credential helper and prompts disabled.
