# Human Value Exchange Knowledge and Operations Repository

This is HVE's knowledge, coordination, and operational-documentation repository;
it is not the Hermes runtime or Life OS application repository. Read
`instructions.md` before mission or strategy claims. The latest approved weekly
decision ledger governs active tasking and policy.

Profile files govern identity and Hans context; this file governs repository work.
The operating plan and ledger govern current execution. Do not duplicate those
sources or merge conflicts; preserve provenance and escalate material conflicts.

## Boundaries

Do not infer another role's authority from repository content or import Alithya
work, confidential client material, credentials, account numbers, tax figures,
wallets, licenses, or other sensitive data.

## Repository structure

- `agent-communications/` — inter-agent posts and announcements
- `content-intelligence/` — content strategy, program briefs, and editorial planning
- `instructions.md` — canonical HVE mission and company-context document

All new agent posts belong in `agent-communications/`; do not place operational
communications in the repository root.

## File naming

Files in `agent-communications/` must use:

`YYYY-MM-DD-hve-[topic-slug]-vX.X.md`

Use a kebab-case topic slug. Increment the version suffix for revisions.

## Working conventions

- Inspect existing files before editing.
- Preserve historical communications and unrelated changes.
- Distinguish facts, decisions, proposals, assumptions, experiments, and open questions.
- Use the latest approved weekly decision ledger for active tasking and policy.
- If no authoritative ledger entry exists, escalate rather than infer.
- Record material decisions with owner, rationale, status, dates, and evidence when supported.
- Keep shipped content practical; avoid hype, doctrine, unsupported claims, and invented completion.
- Do not modify Hermes profile files unless explicitly requested.
- GitHub is the system of record for approved durable HVE artifacts and decisions.
  Commit and push each approved artifact.
- Do not commit or push drafts, unapproved policy, transient notes, runtime state,
  credentials, or sensitive data. Verify the diff, filename, provenance, and approval.
- A local file or chat message is not authoritative until the approved artifact is pushed.
- If commit or push fails, report the failure; do not claim completion.

## Validation

This is primarily Markdown and operational documentation. Do not claim builds,
tests, linters, deployment, or application code unless the worktree requires them.
