# HVE Hermes Agent Card Session Closeout

**Date:** 2026-09-07  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Session closeout and restart handoff  
**Scope:** `hermes-agent-template` Agent Card feature only

## 1. Session outcome

The Agent Card design was approved and translated into a bounded implementation
workflow. AC-1 was implemented by Hermes-coder, reviewed, committed, pushed,
and opened as a draft pull request. Remaining strict validation findings were
explicitly reframed into AC-2 and must be resolved before the draft PR is
merged or the feature is treated as production-ready.

No changes were made to:

- `hve-life-os-alpha`.
- Alpha Phase E.
- Live DGX Spark deployments.
- `hve-chief-of-staff` or any other profile.
- Repository settings or external integrations.

## 2. Approved design and implementation plans

### Design brief

https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-feature-design-v1.0.md

### Implementation plan v1.1

https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-implementation-plan-v1.1.md

### Execution clarification v1.2

https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-implementation-plan-v1.2.md

The v1.2 rules remain authoritative:

- Hermes-coder uses a fresh current-main checkout.
- Hermes-coder edits, tests, and reports only.
- Luna/Hans review, commit, push, and create PRs.
- The card requires all seven mandatory headings.
- Additional headings are allowed only when they do not create competing
  authority.
- No Alpha, Spark, profile, or deployment changes are permitted.

## 3. AC-1 status

### Issue

https://github.com/humanvalueexchange/hermes-agent-template/issues/17

### Draft PR

https://github.com/humanvalueexchange/hermes-agent-template/pull/19

### Commit

`aecaf4b` — `feat: add Agent Card schemas, parser, and fixtures`

### Implemented

- Logical Agent Card schema.
- Logical evidence-manifest schema.
- Importable `schemas.agent_card` parser package.
- Generic `AGENT_CARD.md`.
- Valid and invalid deterministic fixtures.
- Mandatory-heading validation.
- Base frontmatter and evidence parsing.
- Date and timestamp validation work completed during remediation.
- AC-1 parser test suite.

### Validation recorded

```text
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
105 tests passed

PYTHONPATH=. python3 -m unittest discover -s tests -t . -q
160 tests passed

git diff --check
passed
```

The draft PR is not production-ready and must not be merged yet.

## 4. AC-2 status

### Issue

https://github.com/humanvalueexchange/hermes-agent-template/issues/18

AC-2 is the next implementation task and must start in a **brand-new
Hermes-coder session** with a fresh checkout/worktree. Do not resume the
context-heavy AC-1 session.

The remaining review findings assigned to AC-2 are:

1. Enforce actual boolean types for capability flags.
2. Enforce declared string types for identifiers, versions, names, roles, and
   revisions.
3. Normalize valid unquoted YAML dates/timestamps consistently.
4. Convert invalid unquoted YAML date construction failures into structured
   field-specific errors.
5. Attribute invalid `expires_at` errors to `expires_at`, not `checked_at`.
6. Expand canonical-authority heading protection for Tools, Memory,
   Deployment, Approval, Permissions Policy, activation, and related aliases.

AC-2 must receive its own bounded issue budget and must not expand into AC-3 or
AC-4.

## 5. Remaining workflow

After AC-2:

1. Review and validate AC-2.
2. Create and implement AC-3 for security, portability, isolation,
   redaction, and approval-default validation.
3. Create and implement AC-4 for documentation, evidence reporting, and
   integration into `tests/run-all.sh`.
4. Run the complete target validation suite.
5. Merge the implementation only after all four issue gates pass.
6. Open a separate profile-instance issue for `hve-chief-of-staff`.

No profile propagation is part of the current PR.

## 6. Restart instructions for tomorrow

Start a new Luna session with this closeout note and the following references:

- This closeout note.
- The approved design brief.
- Implementation plan v1.1.
- Execution clarification v1.2.
- `humanvalueexchange/hermes-agent-template#18`.
- Draft PR `humanvalueexchange/hermes-agent-template#19`.

Start Hermes-coder separately in a fresh session for AC-2. Use the current
target repository state and preserve the rule that Hermes-coder does not
commit, push, or create PRs.

The immediate decision point tomorrow is whether AC-2 should be implemented as
a dependent stacked change on the AC-1 draft branch or after AC-1 is merged.
The safer default is a dependent stacked change while PR #19 remains draft,
followed by sequential review and merge only after AC-2 passes.

## 7. Final state at closeout

- Design: approved.
- Implementation plan: approved through v1.2 clarification.
- AC-1 implementation: committed and pushed.
- AC-1 PR: draft, not merged.
- AC-2: issue open, not started.
- AC-3: planned, issue not created.
- AC-4: planned, issue not created.
- Profile propagation: not started and not authorized.
- Alpha Phase E: untouched.
- Spark deployment: untouched.
