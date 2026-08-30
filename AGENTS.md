# Human Value Exchange Knowledge and Operations Repository

## Repository purpose

This repository is HVE's knowledge, coordination, and operational documentation
layer. It is not the Hermes runtime, the HVE Life OS application repository, or
a general-purpose software workspace.

Before making mission or strategy claims, read `instructions.md`. Treat the
latest approved weekly decision ledger produced by the Monday 00:07 HVE mission
review workflow as authoritative for active tasking, ownership, dates,
commitments, and policy.

`instructions.md` is authoritative for broad HVE mission and framework context.
It does not override profile identity, current approved operating plans,
decision-ledger events, or explicit CEO decisions. Dated operational details in
it require current-source verification when a newer approved ledger or plan
exists.

## Context layering

- `SOUL.md` defines the active Hermes profile's identity, authority, style, and
  safety boundaries.
- `USER.md` defines Hans's durable profile and working preferences.
- `MEMORY.md` contains durable HVE facts and pointers to authoritative sources.
- This `AGENTS.md` defines how to work inside this repository.
- `instructions.md` provides canonical HVE mission and company context.
- The approved operating plan and weekly decision ledger govern current policy
  and execution.

Do not duplicate the contents of those files here. If sources conflict, do not
improvise a merged interpretation. Follow the higher-authority source for its
domain and escalate material conflicts to Hans.

## Agent boundaries

Do not infer CFO, treasury, CTO, COO, legal, tax, or final-decision authority
from repository content. Agents coordinate within their approved lane; Hans
retains final authority over HVE purpose, values, priorities, commitments, and
decisions.

Do not import Alithya work, confidential client material, credentials, account
numbers, tax figures, wallets, licenses, or other sensitive data into this
repository.

## Repository structure

- `agent-communications/` — inter-agent posts and announcements
- `content-intelligence/` — content strategy, program briefs, and editorial planning
- `instructions.md` — canonical HVE mission and company-context document

All new agent posts belong in `agent-communications/`. Do not place operational
communications in the repository root.

## File naming

Files in `agent-communications/` must use:

`YYYY-MM-DD-hve-[topic-slug]-vX.X.md`

Use a kebab-case topic slug. Increment the version suffix for revisions to an
existing topic.

## Working conventions

- Inspect existing files before editing.
- Preserve historical communications and unrelated changes.
- Distinguish facts, decisions, proposals, assumptions, experiments, and open questions.
- Do not treat chat, external claims, or informal notes as approved policy.
- Use the latest approved weekly decision ledger for active tasking and policy.
- If no authoritative ledger entry exists, escalate rather than infer.
- Record material decisions with owner, rationale, status, effective date, review date,
  and verification evidence when the operating workflow supports it.
- Keep shipped content practical: translate sovereignty or philosophy into a decision,
  observable behavior, or next action.
- Avoid hype, doctrine, unsupported authority claims, generic motivation, and status
  theater.
- Do not invent approvals, commitments, dates, evidence, ownership, or completion.
- Do not modify Hermes profile files from this repository unless explicitly requested;
  profile configuration belongs under the relevant profile directory.
- GitHub is the system of record for approved durable HVE artifacts, decisions,
  and operating documentation. Commit and push each approved artifact as part of
  the normal workflow so it is visible and shareable to humans and agents.
- Do not commit or push drafts, unapproved policy, transient notes, runtime state,
  credentials, or sensitive data. Verify the diff, filename, provenance, and
  approval status before committing.
- A local file or chat message is not authoritative until the approved artifact
  has been successfully committed and pushed to GitHub.
- If commit or push fails, report the failure clearly; do not claim the artifact
  is recorded or complete.

## Validation

This is primarily a Markdown and operational-documentation repository. Do not claim
that builds, tests, linters, deployment systems, or application code exist unless
the current worktree explicitly contains and requires them.
