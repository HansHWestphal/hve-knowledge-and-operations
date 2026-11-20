# HVE x402 Watch — Publication Failures: Findings and Recommendations

- **Date:** 2026-11-20
- **Author:** HVE-Librarian (hve-librarian profile)
- **Status:** Findings + recommendations, **awaiting Hans's decision** — no fixes executed, no publication actions taken.
- **Trigger:** Hans reported that x402 Watch reports had not been published to the website over the last two weeks.

---

## 1. Result (verified 2026-11-20)

The weekly report job `hve-x402-watch-weekly` (cron `0 7 * * 5`, Fridays 07:00 EST) ran all three Fridays in the window. Two reports reached the site; one did not. One site link is broken.

| Run (Friday) | Generated | On live site? | Notes |
|---|---|---|---|
| 2026-11-06 (`20261106T120041.069425Z`, coverage: complete, 19 sources) | 11-06 07:04 EST | **Yes, late** — went live 11-07 01:19 EST (commit `4104bf0`; manifest `published_at` 2026-11-07T06:19:44Z) | Friday's cron output contains no publication line; the publication happened the following ~1:20 AM |
| 2026-11-13 (`20261113T120041.071062Z`, coverage: partial, 5 sources) | 11-13 07:03 EST | **Yes** — commit `db1cb13` at 11-13 07:02:58 EST | **But its archive edition file returns HTTP 404** on the live site (see §3) |
| 2026-11-20 (`20261120T120059.956804Z`, coverage: partial) | 11-20 07:03 EST | **No** — publication refused by the repo-clean guard | Collection and synthesis completed locally; publication failed; only the failure traceback was delivered to Telegram |

Live-site checks (all run 2026-11-20):
- `GET https://hanshwestphal.github.io/x402-watch/data/manifest.json` → 200; latest edition = the 2026-11-13 run.
- `GET https://hanshwestphal.github.io/x402-watch/data/editions/20261106T120041.069425Z.json` → 200
- `GET https://hanshwestphal.github.io/x402-watch/data/editions/20261030T110013.188996Z.json` → 200
- `GET https://hanshwestphal.github.io/x402-watch/data/editions/20261113T120041.071062Z.json` → **404** (referenced by the live manifest, file missing from the public repo)

Local run state (`/hve-library/private/x402-watch/runs/<run>/automation-state.json`):
- 2026-11-13: `publication_status: "published"`
- 2026-11-20: `publication_status: "failed"`, error: `Public repository checkout has unrelated local changes`

## 2. Root cause (two linked defects)

**Defect 1 — publication commit omits the edition file (code gap).**
In `/home/hans/hve-librarian/tools/x402_public.py`, `publish_run()` writes three artifacts into the public checkout — `data/brief.json`, `data/manifest.json`, **and** a new `data/editions/<run_id>.json` — but its commit step hardcodes:

```
git add -- data/brief.json data/manifest.json
```

(the `PUBLIC_FILES` tuple only). The edition JSON is therefore **never staged or pushed**. Verified: commit `db1cb13` (Nov 13) touched only `brief.json` and `manifest.json`; `git ls-files data/` excludes the Nov 13 edition; the working tree still contains it as an untracked file: `?? data/editions/20261113T120041.071062Z.json`. Consequences: (a) the site's manifest/archive references a file that 404s; (b) the file sits untracked in the checkout indefinitely.

**Defect 2 — the stale untracked file fail-closed the Nov 20 publication (guard worked as designed).**
`validate_public_repository()` refuses to publish from a checkout with any local changes. The leftover untracked Nov 13 edition file tripped that guard, so the 2026-11-20 publication was rejected with `PublicProjectionError: Public repository checkout has unrelated local changes`. The Nov 20 report was not lost — collection and synthesis completed; only publication and delivery were blocked.

**Open question (not verified):** why the Nov 6 run also did not publish at 07:04 on Friday and instead landed the next morning at 01:19 EST. The cron output, commit history, and run state do not preserve a record of that specific failure. Flagged plainly rather than inferred.

## 3. Why Hans saw "not published"

- The newest report on the site is the Nov 13 run — today's (Nov 20) report never landed.
- The Nov 13 archive/edition link 404s for anything trying to open it, making the latest publication appear broken.
- (Context) Nov 6's publication is 19+ hours late relative to its scheduled run.

## 4. Recommendations (decision required from Hans)

Ordered, each independently reversible until pushed:

- **A. Complete the interrupted Nov 13 publication.** Commit + push `data/editions/20261113T120041.071062Z.json` — it is already referenced by the pushed public manifest and the run state is `published`. Removes the live 404 and clears the guard. *Effect: pushes to the public site.*
- **B. Publish the Nov 20 report now** (run `20261120T120059.956804Z`, already synthesized) via `x402_public.py --run-dir … --publish`. *Effect: pushes the new brief to the public site.*
- **C. Fix the staging gap in `x402_public.py`** so `publish_run()` also stages the new edition file on commit (or stages all expected changed paths), with a regression check. Prevents recurrence from the next Friday onward. *Effect: code change in the hve-librarian tools repo.*

**Recommended owner:** HVE-Librarian can execute A/B/C under Hans's explicit GO; C's code change should get Luna's (Technical Architect) review given the publication pipeline is shared tooling.

## 5. What was NOT done

No fixes were executed, nothing was pushed for these findings, and no publication was performed. Per Hans's instruction: publish findings and recommendations to agent comms, then stand by.

## 6. Verification record (2026-11-20)

- Cron job state: `~/.hermes/profiles/hve-librarian/cron/jobs.json` → job `f2918d3558ca`, last run 2026-11-20T07:03:55 EST, `last_status: error`, failure traceback as cited.
- Cron outputs: `~/.hermes/profiles/hve-librarian/cron/output/f2918d3558ca/` — Nov 6, Nov 13, Nov 20 run files.
- Run states: `/hve-library/private/x402-watch/runs/*/automation-state.json` as listed in §1.
- Public repo: `/hve-library/public/x402-watch` — `git status`, `git log`, `git ls-files`, commit `db1cb13`/`4104bf0` stats; remote `https://github.com/HansHWestphal/x402-watch.git`, branch `main`.
- Live site: manifest + three edition URLs checked via HTTP status codes as listed in §1.

## 7. Provenance boundary

This document is a diagnostic report of HVE-operated tooling. It does not change policy, tasking, or the decision ledger. Facts are quoted from the cited artifacts above; interpretations (e.g., "the Nov 6 publication likely failed at the guard, similar to Nov 20") are not made because the evidence does not confirm them.
