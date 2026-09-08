# HVE Hermes Agent Card Implementation Plan

**Date:** 2026-09-07  
**Version:** 1.1  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Decision owner:** Hans Westphal, CEO  
**Implementation owner:** Hermes-coder, after issue assignment  
**Target repository:** `humanvalueexchange/hermes-agent-template`  
**Design authority:** [Approved v1.0 design and acceptance brief](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-feature-design-v1.0.md)  
**Supersedes:** [Implementation plan v1.0](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-implementation-plan-v1.0.md)  
**Status:** Ready to become four bounded implementation issues; no issue created

## 1. Purpose and execution rule

This plan is the implementation contract for Hermes-coder. It decomposes the
approved Agent Card design into four bounded issues with explicit dependencies,
schemas, fixtures, commands, acceptance criteria, evidence, and stopping rules.

Hermes-coder must not treat this document as permission to modify the target
repository until the four issues are separately created and assigned.

The implementation is limited to:

```text
humanvalueexchange/hermes-agent-template
```

The following are hard boundaries:

- Do not modify `hve-life-os-alpha`.
- Do not execute or document Alpha Phase E changes.
- Do not modify live Spark state or deployment profiles.
- Do not propagate a card to `hve-chief-of-staff` or another profile.
- Do not add network publication, A2A, Agent 365, registry hosting, or external
  identity provisioning.
- Do not lower or reinterpret the 65,536-token auxiliary-context minimum.
- Do not make AGENT_CARD.md a permission, memory, or runtime authority.

## 2. Issue decomposition and dependencies

Create these issues in `humanvalueexchange/hermes-agent-template` in order:

| Issue | Title | Depends on | Maximum implementation iterations |
|---|---|---|---:|
| AC-1 | Add Agent Card and evidence schemas, parser, and fixtures | None | 3 |
| AC-2 | Add cross-contract and lifecycle validation | AC-1 | 3 |
| AC-3 | Add security, portability, isolation, and approval validation | AC-1 | 3 |
| AC-4 | Add documentation, evidence report, and test-suite integration | AC-2, AC-3 | 2 |

**Total Hermes-coder budget: 11 implementation iterations.**

An iteration is one bounded cycle of inspect, edit, and targeted validation. A
cycle must end with a test result or an explicit blocker. Re-reading,
reformatting, or speculative redesign does not create additional iterations.

After the budget is exhausted, Hermes-coder must stop and report:

- Completed issue and acceptance items.
- Failed or unresolved item.
- Exact command and error.
- Files changed.
- Why another approach was not attempted.

Scope expansion, new dependencies, or changes to authority boundaries require
Luna/Hans approval and do not silently consume more iterations.

## 3. Shared repository rules

These apply to every issue:

- Preserve existing behavior outside the Agent Card feature.
- Use existing Python standard-library and shell-test conventions unless a
  dependency is explicitly approved.
- Do not add a network dependency to validation.
- Do not invoke a model during parsing or validation.
- Do not use `yaml.safe_load` unless the target repository already has an
  approved YAML dependency; otherwise implement only the required frontmatter
  subset or use the repository's existing parser.
- Use profile-relative references, not machine-specific absolute paths, in the
  generic card and fixtures.
- Keep the generic profile disabled by default.
- Do not commit secrets, real credentials, private memory, or live evidence.
- Every issue must link its PR to the issue and post an idempotent proof comment.

## 4. Exact file contract

The implementation should use these paths unless the target repository already
has a clearly superior established convention:

```text
AGENT_CARD.md
schemas/agent-card.schema.yaml
schemas/agent-card-evidence.schema.yaml
agent-card/
    __init__.py
    parser.py
    validation.py
tests/agent_card/
    __init__.py
    fixtures/
        valid-generic-card.md
        valid-generic-evidence.yaml
        invalid-missing-owner-card.md
        invalid-approval-card.md
        invalid-cross-profile-card.md
    test_parser.py
    test_validation.py
docs/evidence/
    agent-card-validation-report-v1.0.md
```

The exact module directory may be adjusted to match the repository's package
layout, but the public behavior and fixture semantics below are mandatory.

## 5. Exact AGENT_CARD.md frontmatter schema

The card is Markdown with a YAML frontmatter block delimited by `---`.
Frontmatter must conform to this logical schema:

```yaml
schema_version: "1.0"
card_revision: "1.0"
agent:
  id: agent-template
  name: Agent Template
  category: template
  owner_role: profile-maintainer
  profile_version: "0.6.1"
  status: disabled
  source_repo: humanvalueexchange/hermes-agent-template
  live_profile_path: null
  last_reviewed: "2026-09-07"
skills:
  - id: reference-behavior
    name: Reference Behavior
    verb: knows
    description: Demonstrates the generic profile contract.
    tags: [reference, generic]
    examples: []
    requires_approval: false
capabilities:
  memory_enabled: true
  approval_required: true
  consultation_enabled: false
  streaming: false
tools: []
references:
  permissions: PERMISSIONS.md#default-deny
  escalation: CHARTER.md#escalates
  memory: MEMORY.md#rules
  evidence_manifest: tests/agent_card/fixtures/valid-generic-evidence.yaml
  decommission: docs/deployment.md#deployment-rules
approval_gates:
  - all consequential actions require explicit confirmation
```

Required keys:

```text
schema_version
card_revision
agent.id
agent.name
agent.category
agent.owner_role
agent.profile_version
agent.status
agent.last_reviewed
skills
capabilities
tools
references.permissions
references.escalation
references.memory
references.evidence_manifest
```

Allowed values:

```text
agent.category:
  time | physical | mental | social | financial | chief-of-staff |
  librarian | template | other

agent.status:
  disabled | standby | operational | deprecated

skills[].verb:
  knows | recommends | creates | acts

skills[].requires_approval:
  boolean
```

`source_repo` and `live_profile_path` are optional. Generic mode must use a
repository identifier rather than a local checkout path, and
`live_profile_path` must be `null` when no profile is installed.

The Markdown body must contain exactly these required headings, with additional
headings permitted only when they do not duplicate authority:

```text
## Purpose & Scope
## Capabilities
## Technology
## Governance
## Memory & Data
## Validation & Evidence
## Limitations & Escalation
```

## 6. Exact evidence-manifest schema

The evidence manifest is YAML and is authoritative for validation detail:

```yaml
schema_version: "1.0"
agent_id: agent-template
profile_version: "0.6.1"
card_revision: "1.0"
source_revision: fixture
checked_at: "2026-09-07T00:00:00Z"
expires_at: "2027-03-06T00:00:00Z"
review:
  owner_role: profile-maintainer
  reviewer: fixture-reviewer
  approval_reference: fixture-only
checks:
  health:
    status: pass
    command: tests/health/check-profile.sh
    evidence: fixture:health
  isolation:
    status: pass
    command: tests/isolation/check-isolation.sh
    evidence: fixture:isolation
  portability:
    status: pass
    command: tests/portability/check-portability.sh
    evidence: fixture:portability
  rollback:
    status: pass
    command: tests/rollback/check-rollback-contract.sh
    evidence: fixture:rollback
known_gaps: []
```

Required keys:

```text
schema_version
agent_id
profile_version
card_revision
source_revision
checked_at
expires_at
review.owner_role
review.reviewer
review.approval_reference
checks.health
checks.isolation
checks.portability
checks.rollback
known_gaps
```

Each check requires:

```text
status: pass | fail | untested
command: non-empty string
evidence: non-empty string
```

The validator must reject `operational` status when any required check is
`fail` or `untested`, when `expires_at` has passed, or when the evidence
manifest does not match the card's agent/profile/card revision.

## 7. Required fixture set

### Valid generic fixture

`valid-generic-card.md` must:

- Parse successfully.
- Use `agent-template`.
- Use owner role `profile-maintainer`.
- Use status `disabled`.
- Use no HVE identity, private path, credential, channel, or external tool.
- Reference `valid-generic-evidence.yaml`.
- Contain one `knows` skill with `requires_approval: false`.

`valid-generic-evidence.yaml` must:

- Match the card identifiers and versions.
- Use a deterministic fixture source revision.
- Pass schema validation.
- Demonstrate all four validation check objects.

### Invalid missing-owner fixture

`invalid-missing-owner-card.md` must fail because `agent.owner_role` is absent
or empty. The failure must identify the exact field.

### Invalid approval fixture

`invalid-approval-card.md` must contain a `creates` or `acts` skill with
`requires_approval: false` and must fail approval-default validation.

### Invalid cross-profile fixture

`invalid-cross-profile-card.md` must contain a forbidden private path or
historical profile reference and must fail portability/isolation validation.

Fixtures must remain synthetic and must not contain live HVE data.

## 8. Issue AC-1 — schemas, parser, and fixtures

### Objective

Introduce the card and evidence schemas, parse frontmatter and evidence
manifests, and establish valid and invalid fixtures without integrating the
full repository validation suite.

### Required changes

- Add the card schema.
- Add the evidence-manifest schema.
- Add parser code with explicit malformed-input errors.
- Add the required fixture set.
- Add parser/schema unit tests.

### Named commands

Run after each implementation iteration:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
```

Run before closing AC-1:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
git diff --check
```

### Acceptance criteria

- Valid card and evidence fixtures parse.
- Required-field failures identify their field.
- Invalid enum and malformed frontmatter failures are explicit.
- Fixture tests do not require network, model access, or HVE adapter state.
- Parser does not silently coerce invalid values into success.
- No existing template test is changed except where required for integration.

## 9. Issue AC-2 — cross-contract and lifecycle validation

### Objective

Validate that a card accurately references the existing template contracts and
that lifecycle status is supported by evidence.

### Required changes

- Match `agent.id` against `PROFILE.yaml`.
- Validate profile version against the selected version policy.
- Resolve tool and governance references.
- Validate evidence-manifest identity and revision matching.
- Implement status gates.
- Implement 180-day evidence freshness.
- Reject operational status with failed, untested, missing, or expired evidence.

### Named commands

```bash
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
PYTHONPATH=. python3 -m unittest discover -s tests/config -t . -q
```

Before closing AC-2:

```bash
tests/health/check-profile.sh
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
git diff --check
```

### Acceptance criteria

- Generic `agent-template` card validates against current `PROFILE.yaml`.
- Broken references fail with file/field context.
- Disabled fixture remains valid without installation evidence.
- Standby requires health, isolation, and portability evidence.
- Operational requires all four checks to pass and evidence to be current.
- Deprecated requires decommission and rollback references.
- A 180-day-old or older evidence manifest cannot establish operational status.
- Material identity/version mismatch fails closed.

## 10. Issue AC-3 — security, portability, isolation, and approval validation

### Objective

Ensure the card cannot disclose secrets, cross profile boundaries, or weaken
the existing permission and approval model.

### Required changes

- Detect credential and secret-like values.
- Reject forbidden profile roots and historical profile fallbacks.
- Reject HVE-specific content in generic fixtures.
- Enforce `knows/recommends/creates/acts` approval defaults.
- Ensure card data cannot activate tools, channels, permissions, or profile
  switching.
- Add portability and isolation tests.

### Named commands

```bash
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
tests/isolation/check-isolation.sh
tests/portability/check-portability.sh
```

Before closing AC-3:

```bash
tests/health/check-profile.sh
tests/isolation/check-isolation.sh
tests/portability/check-portability.sh
PYTHONPATH=. python3 -m unittest discover -s tests/agent_card -t . -q
git diff --check
```

### Acceptance criteria

- Invalid approval fixture fails for the expected skill verb.
- Invalid cross-profile fixture fails with an isolation/portability error.
- Generic valid fixture contains no secret-like or organization-specific data.
- Card validation cannot mutate permission manifests or runtime configuration.
- Card validation cannot enable external channels or tools.
- Existing default-deny policy remains unchanged.
- The auxiliary context minimum remains 65,536 tokens.

## 11. Issue AC-4 — documentation, evidence, and test integration

### Objective

Document the final contract, integrate validation into the existing suite, and
produce reviewable evidence without changing deployment behavior.

### Required changes

- Update the target repository's README or architecture documentation.
- Add the final implementation plan or ADR to the target repository if
  required by its conventions.
- Add `docs/evidence/agent-card-validation-report-v1.0.md`.
- Integrate targeted checks into `tests/run-all.sh` without removing existing
  checks.
- Document the implementation, limitations, and rollback behavior.

### Named commands

```bash
tests/health/check-profile.sh
tests/health/check-memory.sh
tests/isolation/check-isolation.sh
tests/portability/check-portability.sh
tests/rollback/check-rollback-contract.sh
tests/release/check-v061-gates.sh
PYTHONPATH=. python3 -m unittest discover -s tests -t . -q
tests/run-all.sh
git diff --check
```

### Acceptance criteria

- `tests/run-all.sh` passes without removing or weakening existing checks.
- The new card checks run from the existing suite.
- The evidence report names commands, results, source revision, and known gaps.
- Documentation states that the card is not an authority for permissions,
  memory, deployment, or activation.
- Documentation preserves generic mode, profile isolation, rollback, and the
  64K auxiliary-context minimum.
- No live deployment or unrelated profile path is touched.

## 12. Full completion gate

The four issues are complete only when all conditions hold:

1. AC-1 through AC-4 are merged in dependency order.
2. The target repository's `tests/run-all.sh` passes.
3. The full unittest command passes.
4. `git diff --check` passes before merge.
5. The validation report is committed.
6. The generic card and evidence fixtures are committed.
7. The implementation issue contains an idempotent proof comment with:
   - PR URL.
   - Merge commit SHA.
   - Test commands and results.
   - Evidence-report path.
   - Confirmation that Alpha, Spark, and profiles were untouched.
8. Known gaps are explicitly listed.

Passing tests alone do not authorize profile propagation.

## 13. Pull-request requirements

Each issue may use its own PR or a dependency-ordered stacked PR. Every PR
must:

- Link the issue.
- State the bounded issue scope.
- List files changed.
- List commands run.
- Identify any deviation from this plan.
- Confirm no out-of-scope repository or deployment was touched.
- Avoid mixing unrelated cleanup or refactoring.

The final PR must not claim operational readiness for any deployed profile.

## 14. Hard stop conditions

Hermes-coder must stop and report rather than continue when:

- A required schema conflicts with an existing canonical contract.
- A dependency installation appears necessary.
- A test requires network, credentials, a model, Alpha, or Spark.
- A permission or approval boundary would need to be weakened.
- A target file has unrelated user changes that conflict with the task.
- The issue iteration budget is exhausted.
- A proposed feature requires registry hosting, public exposure, or profile
  propagation.

Only Luna/Hans may authorize a revised scope or additional iteration budget.

## 15. Later, separate work

After the template implementation is merged and reviewed, create a separate
issue for the first profile instance:

```text
Create hve-chief-of-staff AGENT_CARD instance from validated template contract
```

That issue must have its own owner-role binding, evidence manifest, profile
references, validation run, and approval. It must not be attached to AC-1
through AC-4 as an implementation subtask.

## Current decision

The four-issue decomposition and hard budget are approved as the recommended
execution shape. The next action, after Hans confirms this v1.1 plan, is to
create AC-1 through AC-4 in `humanvalueexchange/hermes-agent-template`.

No target issue, implementation branch, profile change, Alpha change, or Spark
change has been created by this post.
