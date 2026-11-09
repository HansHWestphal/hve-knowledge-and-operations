# HVE Skill Development Workflow (Pilot Model)

- **Date:** 2026-11-09
- **Status:** Approved workflow for the hve-cfo pilot and default for new fleet skills
- **Decision owner:** Hans Westphal, CEO
- **Intended recipients:** HVE Knowledge Ops (architect); Luna (implementation); target agents (e.g. hve-cfo)
- **Related:** [2026-11-08-hve-cfo-max-credit-score-skill-v1.0.md](2026-11-08-hve-cfo-max-credit-score-skill-v1.0.md) (research note, commit `c45eac9`); [2026-11-08-hve-listed-skills-fleet-addition-backlog-v1.0.md](2026-11-08-hve-listed-skills-fleet-addition-backlog-v1.0.md)

## Purpose

Record the skill development workflow Hans accepted on 2026-11-09, modeled on the hve-cfo **Max Credit Score** skill. That end-to-end path — research → plan → SKILL.md → synthetic UAT → go-live → Hans acceptance UAT on a real document → HTML outbox deliverable — is the model to follow for the pilot and going forward.

## DECISION

**DECISION (Hans, 2026-11-09):** Use the Max Credit Score workflow as the standard HVE skill development flow for the hve-cfo pilot and as the default for new fleet skills. Architect (HVE Knowledge Ops) scopes and prompts; Luna plans and implements; the target agent runs UAT; Hans approves each gate and supplies the acceptance document.

## Roles and flow

1. **Hans (owner / decider)** — states the need and approves each gate.
2. **HVE Knowledge Ops (architect)** — writes the source research note in this repo (for Max Credit Score: [2026-11-08-hve-cfo-max-credit-score-skill-v1.0.md](2026-11-08-hve-cfo-max-credit-score-skill-v1.0.md), commit `c45eac9`); defines scope and guardrails; drafts Luna prompts for each gate; reviews Luna's plan and drafts; pins public citation URLs.
3. **Luna (implementation engineer)** — writes the implementation plan (plan-only, no build) for Hans/architect review; answers open decisions; drafts `SKILL.md`; revises; after authorization, stages the skill in the agent's repo and the verified live loader path; runs static checks and synthetic UAT. Luna never runs `sudo`; she writes exact commands, Hans runs them and pastes the output.
4. **Target agent (e.g. hve-cfo)** — executes UAT: first a synthetic-fixture UAT against a written pass checklist, then Hans's acceptance UAT on a real document he supplies.
5. **Hans accepts UAT** — skill goes live as on-demand; approved commits are pushed to the agent repo.

## Gates (each needs Hans's approval)

1. Research note in this repo
2. Implementation plan review
3. `SKILL.md` review (open questions resolved; citations pinned)
4. Build authorization with synthetic-UAT-only constraint
5. Synthetic UAT pass
6. Go-live + push to the agent repo
7. Hans acceptance UAT on a real document he supplies

Do not skip gates. Do not invent completion.

## Runtime pattern that worked (FACT — hve-cfo)

**FACT:** For Max Credit Score on hve-cfo:

- Hans drops a document in the agent's inbox (`/srv/hve-inbox/cfo`, read via `read_cfo_inbox`).
- The agent parses it and applies the skill locally (local Hermes + local Ollama only).
- The agent publishes the result as a self-contained HTML deliverable to the agent's outbox via `write_cfo_deliverable`.
- The deliverable is viewable over Tailscale Serve (never Funnel).

That inbox → skill → HTML outbox path is the runtime model for this pilot.

## Lessons from Max Credit Score

- **Launch as the agent user, default-only.** Run as the agent's own Linux user with `HERMES_HOME` set to that user's home and **no** `--profile`. A wrong-user launch caused an "install state not writable" false block that looked like a missing Hermes install.
- **Do not invent tool names in UAT scripts.** Use the projected `mcp__<server>__<tool>` names the live agent actually exposes.
- **Keep synthetic UAT free of real data.** No real scores, inbox files, or spillover sources in the synthetic gate.
- **Skill stays in its domain.** Personal vs HVE Business separation; no cross-domain mixing unless Hans explicitly asks.
- **No autonomous external actions.** Advisory only; no disputes, applications, payments, filings, or ledger posts without Hans.

## Timeline (FACT — Max Credit Score)

| Event | When / evidence |
| --- | --- |
| Research note pushed | commit `c45eac9` (2026-11-08) |
| Local skill commit in hve-cfo repo | `a6aff14` |
| Synthetic UAT passed | 2026-11-08 |
| Hans authorized go-live and push | 2026-11-08 |
| Hans accepted UAT | 2026-11-09 |

## Scope

- **Applies now:** hve-cfo pilot, including Max Credit Score as the reference skill.
- **Default going forward:** new fleet skills follow this workflow unless Hans overrides for a specific item.
- **PROPOSAL:** Reuse this workflow for hve-clo issue #54 and for backlog skills ([2026-11-08-hve-listed-skills-fleet-addition-backlog-v1.0.md](2026-11-08-hve-listed-skills-fleet-addition-backlog-v1.0.md)) when Hans opens them. This note does **not** open those items.

## What this is not

- Not authorization to process real personal or business data beyond what Hans supplies for a named UAT or live run.
- Not a change to Hermes runtime, Git identity, or sudo rules.
- Not install authorization for backlog skills.
- Not a substitute for the existing stack filter or domain boundaries.

## Evidence

- Hans direction in session 2026-11-09: Max Credit Score flow (architect ↔ Luna ↔ hve-cfo ↔ Hans UAT; inbox document → analysis → HTML outbox) is the model to follow for the pilot and going forward.
- Prior Max Credit Score research note and timeline above.

---

*Approved workflow record. Commit and push is the system of record.*
