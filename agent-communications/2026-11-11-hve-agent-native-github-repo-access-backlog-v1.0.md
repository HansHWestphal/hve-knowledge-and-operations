# HVE Agent Native GitHub Repo Access — Backlog v1.0

- **Date:** 2026-11-11
- **Author:** HVE Knowledge Ops
- **Status:** BACKLOG — not authorized to build or configure
- **Decision owner:** Hans
- **First agent:** hve-cfo → `humanvalueexchange/hve-cfo`; then each fleet agent as it moves to its own Linux user

## 1. Request (Hans, 2026-11-11)

FACT: Hans wants every HVE fleet agent to read and write its own GitHub repo natively, starting with hve-cfo. The goal is that the agent writes UAT results directly to GitHub, Luna and HVE Knowledge Ops read them there, and Hans no longer relays outputs by copy-paste.

FACT: Hans placed this on the backlog. Priority order: (1) best-mortgage-rate skill deployed and tested, (2) Arete-27B deployment on the Spark, then this item.

## 2. Current state (hve-cfo self-report, 2026-11-11)

FACT, as reported by hve-cfo:

| Check | Result |
|---|---|
| Runtime identity | user `hve-cfo` (uid 1001); groups `hve-cfo`, `hve-cfo-inbox-read`; not in `hans` group |
| Working tree `/home/hve-cfo/repos/hve-cfo` | owned `hans:hans`, mode 775 → CFO is "other" (r-x): can read, cannot create or modify files |
| `.git` directory | owned by `hve-cfo` (mixed ownership with the working tree) |
| git safety check | flags "dubious ownership" (`safe.directory` would only silence the check, not grant write) |
| GitHub auth | `gh`: not logged into any host; no credential helper or token |
| Net effect | CFO can read the repo, cannot commit locally, cannot push |

ASSUMPTION: the mixed ownership (`.git` = hve-cfo, files = hans) is a leftover from the 2026-11-04 default-profile migration. It should be resolved to a single owner when this item is opened.

CFO offered three options; none was chosen:
1. Make the tree writable to CFO (chown to `hve-cfo`, or group/mode change) — local commits only.
2. GitHub auth (gh login, PAT, or SSH key scoped to the repo) — commit and push.
3. No access change — CFO writes a patch in scratch space for someone to apply.

## 3. Proposal (for when Hans opens this)

PROPOSAL: options 1 + 2 together, with guardrails. Option 3 keeps the manual relay this item exists to remove.

1. **Single owner.** `hve-cfo` owns its working tree (`/home/hve-cfo/repos/hve-cfo`) end to end. Hans runs the ownership change (sudo).
2. **Per-agent GitHub identity.** A GitHub App (preferred over a personal PAT) installed only on the agent's own repo, with Contents read/write only — no admin, no workflows, no other repos. Short-lived installation tokens; commits attributable to the agent; revocable per agent. Private key stored in the agent's home, mode 0600, owned by the agent user; installed by Hans.
3. **No pushes to `main`.** The agent writes to a `uat/*` branch (or a `uat-results/` path on that branch). Branch protection on `main` enforces it. Code still lands via Luna with Hans's approval.
4. **Personal-data gate (critical for CFO).** Synthetic UAT results may be pushed in full. Acceptance UAT on Personal-domain skills (Max Credit Score, best-mortgage-rate) pushes only a redacted pass/fail summary — no scores, balances, rates, dates, identifiers, or inbox file contents. A pre-push check blocks anything resembling personal values. Personal and HVE Business data stay separate.
5. **Rollout.** hve-cfo first as a pilot; Librarian and COS follow their own Linux-user migrations.

## 4. Constraints carried forward

- Local first, then GitHub; GitHub and Proton remain the only trusted partners.
- Hans runs every sudo command; Luna writes exact commands and waits for pasted output.
- No cloud models, no Funnel, no credentials in any repo or chat.

## 5. Open questions for Hans at pickup

- GitHub App vs fine-grained PAT (recommend App).
- Results location: `uat/*` branches vs a dedicated `uat-results/` folder.
- Whether HVE Knowledge Ops and Luna get read access via existing access or a separate read identity.
