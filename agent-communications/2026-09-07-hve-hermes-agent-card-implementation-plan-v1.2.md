# HVE Hermes Agent Card Implementation Plan — Clarifications

**Date:** 2026-09-07  
**Version:** 1.2  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Decision owner:** Hans Westphal, CEO  
**Target repository:** `humanvalueexchange/hermes-agent-template`  
**Supersedes conflicting wording in:** [v1.1 implementation plan](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-implementation-plan-v1.1.md)  
**Status:** Ready for AC-1 issue creation and supervised Hermes-coder execution

## Purpose

This v1.2 post is an authoritative clarification of the v1.1
implementation plan. It does not change the four-issue decomposition, schemas,
fixtures, acceptance criteria, or 11-iteration total budget. It resolves three
execution ambiguities before AC-1 is assigned.

Hermes-coder must read both v1.1 and this v1.2 clarification. Where wording
conflicts, this v1.2 post controls.

## 1. Execution checkout and branch authority

Hermes-coder must use a fresh checkout of the current `main` branch in the
target repository:

```text
https://github.com/humanvalueexchange/hermes-agent-template
```

The local checkout previously found by HVE is stale and must not be used as the
implementation source. In particular, it reports profile version `0.1.0` and
does not contain the current `tests/run-all.sh`.

### Required preflight

Before editing, Hermes-coder must execute:

```bash
git clone https://github.com/humanvalueexchange/hermes-agent-template.git \
  /tmp/hermes-agent-template-ac1
cd /tmp/hermes-agent-template-ac1
git fetch origin main
git rev-parse origin/main
git status --short --branch
test -f tests/run-all.sh
grep -n 'version:' PROFILE.yaml
```

The exact temporary path may differ, but the checkout must be fresh or must be
proven clean and current against `origin/main`. Hermes-coder must report:

- `origin/main` commit SHA.
- Profile version observed in `PROFILE.yaml`.
- Presence and path of `tests/run-all.sh`.
- Clean/dirty status before editing.

If the checkout does not match the current target `main` contract, Hermes-coder
must stop and report the mismatch. He must not reset, overwrite, or reuse a
stale working tree containing unknown changes.

All four implementation issues must be based on the same current target
`main` lineage or on a clearly documented dependency chain of merged commits.

## 2. Commit, push, and pull-request authority

Hermes-coder is authorized to:

- Inspect the target repository.
- Edit files in the assigned issue scope.
- Run named tests and validation commands.
- Prepare a working diff.
- Report results, blockers, and deviations.

Hermes-coder is **not** authorized under this task contract to:

- Commit changes.
- Push changes.
- Create or merge a pull request.
- Modify repository settings.
- Create deployment changes.

This preserves Hermes-coder's current safety rule requiring approval before
commit/push and avoids conflicting repository ownership actions.

After Hermes-coder reports a complete bounded issue, Luna/Hans will:

1. Review the diff and command results.
2. Confirm the issue acceptance criteria.
3. Create the commit with the required repository trailer.
4. Push the approved branch.
5. Create the pull request.
6. Post or update the proof comment after review.

If the target repository's operating rules later authorize Hermes-coder to
commit or open a PR, that requires an explicit task-specific approval and must
not be inferred from this plan.

The issue must therefore use the lifecycle:

```text
Hermes-coder edits/tests/reports
        ↓
Luna/Hans reviews and approves diff
        ↓
Luna/Hans commits/pushes/opens PR
        ↓
Review and merge gate
```

## 3. Markdown heading rule

The AGENT_CARD.md body must contain all seven mandatory headings:

```text
## Purpose & Scope
## Capabilities
## Technology
## Governance
## Memory & Data
## Validation & Evidence
## Limitations & Escalation
```

Additional headings are **allowed**, but only when all of the following are
true:

- They do not duplicate a mandatory heading.
- They do not create a second source of truth.
- They do not override or weaken an existing canonical contract.
- They provide genuinely useful explanatory content.
- They remain within the card's summary purpose.

The parser/validator must reject a card missing any mandatory heading. It must
not reject additional non-conflicting headings solely because they are
additional.

The documentation must state that headings such as `Permissions`, `Memory
Policy`, or `Deployment Authority` must not become competing contract sections;
they should link to the existing canonical files instead.

## 4. AC-1 issue additions

The AC-1 issue must include these preflight acceptance items:

- [ ] Fresh checkout is based on current `origin/main`.
- [ ] `tests/run-all.sh` exists in the checkout.
- [ ] Observed `PROFILE.yaml` version is recorded.
- [ ] Pre-edit worktree status is recorded.
- [ ] No stale local checkout is used.
- [ ] Hermes-coder has edit/test/report authority only.
- [ ] Commit, push, and PR actions remain with Luna/Hans unless separately
      approved.

AC-1 must add a parser test proving:

- All seven mandatory headings are accepted.
- A missing mandatory heading fails with its heading name.
- Additional non-conflicting headings are accepted.
- An additional heading that attempts to replace or duplicate a canonical
  contract is rejected or reported as a validation error.

## 5. Issue-wide execution commands

Every issue begins by confirming the current checkout:

```bash
git fetch origin main
git rev-parse origin/main
git status --short --branch
test -f tests/run-all.sh
```

Hermes-coder must not claim validation against an unavailable or stale
`tests/run-all.sh`.

Issue-specific commands remain those named in v1.1:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
tests/health/check-profile.sh
tests/isolation/check-isolation.sh
tests/portability/check-portability.sh
tests/rollback/check-rollback-contract.sh
tests/release/check-v061-gates.sh
PYTHONPATH=. python3 -m unittest discover -s tests -t . -q
tests/run-all.sh
git diff --check
```

If a named command does not exist in the current `main` checkout, Hermes-coder
must report that fact instead of inventing a successful result or substituting
an unapproved command.

## 6. Final authority and readiness

This v1.2 clarification does not authorize implementation by itself. It makes
the plan ready for the next governance step:

1. Create AC-1 in `humanvalueexchange/hermes-agent-template`.
2. Link the approved v1.0 design brief, v1.1 implementation plan, and this v1.2
   clarification.
3. Assign Hermes-coder the bounded AC-1 task.
4. Require the fresh-main preflight before any edit.
5. Review the resulting diff before Luna/Hans commits or opens a PR.

No target issue, implementation branch, commit, pull request, profile change,
Alpha change, or Spark change has been created by this clarification post.
