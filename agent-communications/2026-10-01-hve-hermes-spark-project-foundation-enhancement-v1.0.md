# HVE Enhancement Entry — Spark Hermes project foundation

**File:** `agent-communications/2026-10-01-hve-hermes-spark-project-foundation-enhancement-v1.0.md`  
**Date:** 2026-10-01  
**From:** Mika (Grok), on request from Hans Westphal (CEO)  
**To:** Hermes (Spark), Luna, Atlas, and the operating record  
**Status:** Aspiration. Owner-attested as a candidate only. NOT policy, NOT funded, NOT scheduled, NOT an approved commitment.

---

## Source

Community note from @HermesWatcher (unofficial, not Nous Research), 2026-09-29:

https://x.com/hermeswatcher/status/2104919128230273501

HermesWatcher is a release tracker. This is a layout convention, not a Nous release note and not v0.22.

Official Hermes already loads project context. Priority is `.hermes.md` / `HERMES.md` (walks parents to git root), then `AGENTS.md` (cwd only, portable), then `CLAUDE.md`, then Cursor rules. `SOUL.md` is identity and stays separate. Do not put project rules in `~/.hermes/AGENTS.md`.

## Proposal

Give Spark Hermes a default project foundation it can scaffold, then specialize only when an area earns it.

Root files:

- `AGENTS.md` — how agents operate in this project. Root rules apply everywhere.
- `PROJECT.md` — goal, scope, definition of done.
- `STATUS.md` — current state and next steps. Rewritten, not appended forever.
- `DECISIONS.md` — choices that must not die in old chats. One line when a decision is actually made.

Folders:

- `inbox/` — new material lands first.
- `areas/<name>/` — natural sections of this project. A nested `AGENTS.md` is optional and only added when that area is complicated enough.
- `resources/` — files, references, assets, data.
- `work/queued|active|completed/` — stage, not a second ticket system.
- `outputs/` — finished or review-ready.
- `archive/` — old or replaced, kept out of the active tree.

Scaling rule: start with the root four files. Add a local `AGENTS.md` only when complexity earns it. Repeat one level down only if that level earns it.

## Why it fits Spark Hermes

HVE is already multi-area: Spark/Hermes runtime, IG factory, content, tax/wealth, wellness, Bitcoin. Those should not share one prompt.

The IG factory already uses `inbox/`, `work/<slug>/`, and `outbox/`. This is the same grammar one level up, not a new religion.

`DECISIONS.md` is the missing durable surface for choices that currently live only in long sessions (model routing, FOSS-only on Spark, corp and HSA boundaries).

Profiles stay the agent. These files stay with the project. Any profile pointed at the folder can read the same foundation.

## Spark-specific constraints

- Local-first. No cloud fallback. Scaffold must work on the DGX Spark path (`/data/hve` or `$HOME/hve`).
- Do not invent process. Root `AGENTS.md` should say: read `PROJECT.md`, `STATUS.md`, and `DECISIONS.md` first; do not add rules that were not decided.
- Name area folders after the work (`spark-hermes/`, `ig-factory/`, `tax-wealth/`). Do not use PARA's word "Areas" as the folder name if that collides with an existing PARA tree.
- For code repos, git branches remain the work queue. `STATUS.md` points at PRs. Do not duplicate branch state inside `work/`.
- For content and ops (IG factory, intake), `work/queued|active|completed/` is fine.
- Nested `AGENTS.md` is how Spark-local rules (Ollama trio, no Canva/CapCut, Syncthing outbox, FOSS only) stay out of the HVE charter.
- Empty files are not a system. Value is `STATUS.md` rewritten each session and `DECISIONS.md` appended only on a real decision.

## Suggested first cut, if approved later

1. One real HVE root on Spark, not a toy. Four files plus empty dirs.
2. Root `AGENTS.md` that points Hermes at the other three files and forbids invented process.
3. Optional Hermes skill `init-project-foundation` that writes the same scaffold into a new folder in one command.
4. Do not retrofit the Hermes source repo or the CFO runtime until the content/ops root has survived a week.

## Decision required (Hans)

1. Accept as an enhancement candidate for Spark Hermes, owner Hans, not scheduled.
2. Name the first real root (HVE ops vs IG factory vs a new `/data/hve/projects` parent).
3. Confirm skill vs hand scaffold for the first cut.

Until that decision, Hermes should not create this tree, should not treat this note as operating policy, and should not migrate existing inboxes.

---

**Recommendation:** keep as a backlog candidate. Prove it on one content/ops root before any runtime change.
