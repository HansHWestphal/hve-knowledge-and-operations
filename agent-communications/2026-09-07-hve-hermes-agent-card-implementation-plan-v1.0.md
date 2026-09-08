# HVE Hermes Agent Card Implementation Plan

**Date:** 2026-09-07  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Decision owner:** Hans Westphal, CEO  
**Implementation owner:** Hermes-coder, after issue assignment  
**Target repository:** `humanvalueexchange/hermes-agent-template`  
**Design authority:** [HVE Hermes Agent Card Feature Design and Acceptance Brief](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-07-hve-hermes-agent-card-feature-design-v1.0.md)  
**Status:** Approved planning artifact; implementation issue not yet created

## 1. Purpose

This post translates the approved feature design into an implementation-ready
plan for the reusable `hermes-agent-template` repository.

It defines how Hermes-coder should implement and validate the portable
`AGENT_CARD.md` blueprint and evidence-reference contract. It does not itself
authorize implementation, profile backfill, deployment, Alpha Phase E, or
Spark changes.

## 2. Scope

### In scope

- A versioned `AGENT_CARD.md` contract.
- A separate validation evidence-manifest contract.
- Schema and cross-contract validation.
- Capability-verb approval-default enforcement.
- Lifecycle status gates.
- Redaction, portability, and isolation checks.
- Generic `agent-template` reference fixtures.
- Documentation and targeted tests.

### Out of scope

- Changes to `hve-life-os-alpha`.
- Alpha Phase E execution or documentation changes.
- Live Spark deployment or validation.
- Profile propagation or `hve-chief-of-staff` backfill.
- Public registry hosting.
- A2A protocol adoption.
- Microsoft Agent 365 integration.
- Network publication or external identity provisioning.
- Changes to the 65,536-token auxiliary-context minimum.
- Changes to existing permission, memory, deployment, or profile ownership
  behavior unrelated to card validation.

## 3. Implementation order

Hermes-coder should execute the work in the following order:

1. Inspect the current template contracts and existing test conventions.
2. Record the implementation plan in the target repository if required by its
   issue or review process.
3. Define the card schema and evidence-manifest shape.
4. Add a valid generic reference card fixture.
5. Implement schema parsing and validation.
6. Implement cross-contract consistency checks.
7. Implement lifecycle and evidence freshness checks.
8. Implement skill-verb approval-default checks.
9. Implement security, redaction, portability, and isolation checks.
10. Add targeted tests and integrate them into the existing validation suite.
11. Run the full existing template validation command.
12. Produce the evidence report and proof comment.

The implementation must stop and escalate if the current repository contracts
cannot support a requirement without changing their authority model.

## 4. Proposed target-repository artifacts

The implementation issue should be created in
`humanvalueexchange/hermes-agent-template` and should link this post and the
approved design brief.

The expected implementation artifacts are:

```text
AGENT_CARD.md
docs/
└── agent-card-implementation-plan-v1.0.md
tests/
└── agent_card/
docs/evidence/
└── agent-card-validation-report-v1.0.md
```

The exact paths may follow existing target-repository conventions. Hermes-coder
must not create duplicate documents if an existing contract or ADR can be
extended cleanly.

## 5. Card contract

The card should use a small YAML frontmatter block followed by Markdown
narrative. It must summarize existing contracts rather than become a second
source of truth.

### Required stable metadata

- `agent_id`
- display name
- category
- accountable owner role
- schema version
- profile release version reference
- card revision
- lifecycle status
- declared skills
- capability flags
- tool references
- permission and approval references
- escalation reference
- memory/data reference
- evidence-manifest reference
- decommission reference where applicable
- last reviewed date

### Required narrative sections

- Purpose and Scope.
- Capabilities.
- Technology and prerequisites.
- Governance.
- Memory and Data.
- Validation and Evidence.
- Limitations and Escalation.

The card must clearly distinguish declared, approved, enabled, validated, and
operational state.

## 6. Evidence-manifest contract

Detailed runtime and validation state belongs in a separate evidence manifest,
not in a large or frequently changing card.

The manifest should record:

- Evidence schema version.
- Agent ID and profile release version.
- Card revision evaluated.
- Source revision or commit.
- Validation commands or procedures.
- Pass/fail results.
- Execution timestamps.
- Reviewer or approver.
- Evidence paths or URLs.
- Integrity hashes where practical.
- Known gaps.
- Expiry date.
- Material changes that invalidate the evidence.

The card may summarize evidence state, but the manifest is authoritative for
validation detail.

## 7. Rules to implement

### 7.1 Ownership

The required owner is an accountable role. A named human, sponsor, publisher,
or adapter-specific binding may be represented separately later.

The card must not require a HVE-specific person or organization in generic
mode.

### 7.2 Versioning

Keep these concepts independent:

- Schema version.
- Profile release version.
- Card revision.

Documentation-only card changes must not imply runtime changes.

### 7.3 Skill verbs

Supported verbs are:

- `knows`
- `recommends`
- `creates`
- `acts`

Validation defaults:

- `knows` and `recommends` do not require consequential-action approval by
  default.
- `creates` and `acts` require approval by default.

Existing permission manifests remain authoritative. The card validator must
reject an unapproved exception rather than granting one.

### 7.4 Lifecycle

`disabled` means source-only and not installed or active.

`standby` requires health, isolation, and portability evidence, while remaining
disabled from live traffic and scheduled work.

`operational` requires health, isolation, portability, and rollback evidence,
current ownership review, and non-expired evidence.

`deprecated` requires decommission and rollback references.

### 7.5 Review freshness

The default maximum review age is 180 days. Material changes to identity,
permissions, tools, adapter, routing, data boundary, deployment, or external
exposure invalidate affected evidence immediately.

## 8. Validation and test plan

### Schema tests

- Valid generic card parses.
- Missing required fields fail.
- Invalid enums, dates, versions, and statuses fail.
- Unsupported schema versions fail closed.
- Duplicate skill IDs fail.
- Unsupported skill verbs fail.

### Cross-contract tests

- `agent_id` matches `PROFILE.yaml`.
- Profile release reference is valid.
- Tool references resolve.
- Permission, approval, escalation, memory, and decommission references
  resolve.
- Evidence-manifest reference resolves.
- Card status is compatible with evidence.
- Approval defaults match skill verbs.

### Security and isolation tests

- Secret-like values and credential material are rejected.
- Generic cards contain no HVE-specific paths, identity, channels, or
  credentials.
- Forbidden cross-profile roots and historical fallbacks are rejected.
- The card cannot activate tools, channels, permissions, or profile switching.
- External publication metadata is absent or disabled in generic mode.

### Lifecycle tests

- `disabled` accepts source-only state.
- `standby` fails without required health, isolation, and portability evidence.
- `operational` fails with any failed or expired required evidence.
- `deprecated` fails without decommission and rollback references.
- Evidence older than 180 days fails operational readiness.

### Portability and rollback tests

- Generic mode validates without an HVE adapter.
- Validation works from a different checkout path.
- No test writes to live Alpha or Spark paths.
- Removing the card feature does not change existing runtime behavior.
- Evidence can be rebuilt deterministically.

## 9. Compatibility and safety requirements

The implementation must preserve:

- Profile isolation and explicit profile context.
- Adapter boundaries.
- Default-deny permissions.
- Existing approval handoffs.
- SQLite/FTS5 memory authority.
- Existing deployment and rollback contracts.
- The 65,536-token auxiliary-context minimum.
- Disabled-by-default generic profile behavior.

No card parser or validator may make model calls, require network access, or
activate runtime services during ordinary validation.

## 10. Hermes-coder task contract

When the target issue is created, the implementation prompt should require
Hermes-coder to:

- Work only in `humanvalueexchange/hermes-agent-template`.
- Read the approved design brief and this implementation plan first.
- Make no changes to Alpha, Spark, or deployed profiles.
- Use existing repository conventions and validation commands.
- Keep the implementation narrowly scoped.
- Report deviations before broadening scope.
- Run targeted tests after each logical implementation stage.
- Run the full existing validation suite before completion.
- Stop when the acceptance criteria and evidence requirements are satisfied.
- Avoid speculative registry, network, or vendor-integration work.

The issue should define an explicit iteration limit and require escalation
instead of silent scope expansion.

## 11. Completion evidence

The implementation is not complete until the target issue contains:

1. A link to the merged pull request.
2. The merged commit SHA.
3. Validation commands and results.
4. The evidence-manifest location.
5. The validation-report location.
6. Confirmation that generic portability passed.
7. Confirmation that Alpha, Spark, and deployment profiles were untouched.
8. Any known limitations or deferred work.

The proof comment should be idempotent and updated rather than duplicated.

## 12. Approval gates

### Gate A — Design

Completed. The approved design brief is published in the HVE control-plane
repository.

### Gate B — Implementation authorization

Required before creating or assigning the target implementation issue.
Approval confirms this plan is sufficiently precise for Hermes-coder.

### Gate C — Pull-request review

Required before merge. Review must cover code correctness, contract authority,
security, portability, evidence, and scope isolation.

### Gate D — Template readiness

Required after merge. The template implementation and evidence must pass review
before any profile receives a propagated card.

### Gate E — Profile instance

Separate issue and approval required for the first `hve-chief-of-staff` card
instance. This gate must not be combined with template implementation.

## 13. Non-goals and deferred expansion

The following are intentionally deferred:

- Repository- or organization-level registry aggregation.
- Signed external publication.
- A2A or Agent 365 protocol integration.
- Public capability discovery.
- Automated profile activation.
- Automatic permission provisioning.
- Runtime status mutation from inference activity.
- Backfill of existing live profiles.

These may become later proposals after the MVP has been implemented and
validated.

## Recommended next workflow step

After Hans approves this implementation plan:

1. Create the implementation issue in
   `humanvalueexchange/hermes-agent-template`.
2. Link the issue to the approved design brief and this plan.
3. Assign the issue to Hermes-coder with the scoped task contract.
4. Require the target-repository implementation plan or ADR before coding if
   the repository's review process needs a local copy.
5. Review the resulting pull request and evidence before merge.

**Current status:** No target issue has been created. No implementation has
started. No profile, Alpha, or Spark changes are authorized by this post.
