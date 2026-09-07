# HVE Hermes Agent Card Feature Design and Acceptance Brief

**Date:** 2026-09-07  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Decision owner:** Hans Westphal, CEO  
**Target repository:** `humanvalueexchange/hermes-agent-template`  
**Status:** Design approved for implementation specification; implementation not yet approved  
**Scope:** Reusable template contract only

## Executive decision

HVE approves development of a proper design and acceptance artifact for a
portable `AGENT_CARD.md` contract in `hermes-agent-template`.

The feature is a reusable **agent blueprint and evidence-reference contract**.
It is not a replacement for `PROFILE.yaml`, `SOUL.md`, `CHARTER.md`,
`PERMISSIONS.md`, `MEMORY.md`, `TOOLS.md`, or runtime configuration. It must
not grant permissions, activate tools, publish a profile, or infer operational
readiness.

Implementation must be completed and validated in
`humanvalueexchange/hermes-agent-template` first. Only after that work is
merged and its evidence is reviewed may the card be propagated to deployment
profiles. This feature must not modify `hve-life-os-alpha`, Phase E, or live
Spark deployments during design or template implementation.

## 1. Problem

Hermes profiles currently express identity, purpose, ownership, tools,
permissions, memory, configuration, validation, and lifecycle state across
several separate contracts. The separation is architecturally correct, but a
human or orchestrator cannot quickly determine whether a profile is suitable
and safe to route work to without opening and reconciling multiple files.

The proposed `AGENT_CARD.md` provides a small, predictable summary layer that
answers:

- What is this agent and what is its bounded purpose?
- What capabilities does it declare?
- Who is accountable for it?
- What tools, data, memory, and approval boundaries apply?
- What limitations and escalation rules apply?
- Which validation evidence supports its current lifecycle status?
- Is it disabled, standby, operational, or deprecated?

## 2. Customer and operator value

The immediate value is operational trust and fleet governance. An operator can
review a profile at a glance while retaining links to authoritative contracts
and detailed evidence.

Potential fundable value includes:

- Reducing the time required to review and onboard an agent.
- Making agent ownership and lifecycle accountability explicit.
- Preventing undocumented or over-privileged capabilities from being treated as
  available.
- Providing a portable governance artifact for heterogeneous agent runtimes.
- Creating a foundation for a future agent registry without requiring a
  network service now.
- Making a small-footprint control-plane pattern portable to larger enterprise
  governance systems.

The differentiation is the combination of:

- A2A-style machine-readable skill discovery.
- Model-card-style limitations and evaluation transparency.
- Enterprise agent-profile ownership and approval gates.
- Local-first privacy and portability.
- Validation, provenance, and rollback evidence.

HVE must not claim A2A compliance or Microsoft Agent 365 integration from this
feature alone. The design is forward-compatible with those concepts, not a
commitment to external publication or a vendor protocol.

## 3. Architectural placement

The feature belongs in the reusable `hermes-agent-template` because the
problem is common to every independently deployable profile: identity,
capability discovery, accountability, governance references, and readiness
evidence.

The template owns:

- The card schema and contract.
- Required fields and lifecycle semantics.
- Cross-contract consistency rules.
- Skill metadata and approval-default rules.
- Evidence-manifest format and validation requirements.
- Portability, redaction, and isolation checks.
- Future registry compatibility.

Deployment instances or organization adapters supply:

- The accountable owner-role binding.
- Organization identity and policy.
- Live profile paths and runtime locations.
- Enabled channels, tools, and adapters.
- Deployment-specific validation evidence.
- Current operational state.

The card must not hard-code HVE-specific identity, credentials, private paths,
organization data, or another profile's runtime state.

## 4. Microsoft Agent 365 alignment

Microsoft Agent 365 provides a useful control-plane comparison. Its current
model separates:

| Microsoft concept | Hermes design equivalent |
|---|---|
| Agent identity blueprint | Template contract and card schema |
| Agent identity/instance | Deployed Hermes profile instance |
| Agent Registry | Future HVE profile registry |
| Identity and consent | Hermes permission manifests and approval handoffs |
| Observability | Evidence manifest and local analytics |
| Lifecycle governance | Status lifecycle, review, activation, and rollback gates |
| External publication | Separate sanitized external descriptor |

Microsoft's documented principles that directly inform this design are:

- A reusable blueprint is distinct from each deployed agent identity.
- Ownership and sponsor accountability are lifecycle controls.
- Declared resource access does not itself grant authorization.
- Registry metadata is distinct from changing operational and risk evidence.
- External agents can be onboarded without replacing their underlying runtime.
- Observability must cover agent invocation, inference, and tool activity.

Sources consulted:

- [Microsoft Agent 365 overview](https://learn.microsoft.com/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)
- [Agent identity blueprints](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-blueprint)
- [Agent Registry](https://learn.microsoft.com/microsoft-365/admin/manage/agent-registry)
- [Connect existing agents](https://learn.microsoft.com/microsoft-agent-365/connect-existing-agents)
- [Agent 365 development quickstart](https://learn.microsoft.com/microsoft-agent-365/developer/get-started)
- [Agent 365 observability](https://learn.microsoft.com/microsoft-agent-365/admin/monitor-agents)

## 5. Proposed MVP

The MVP consists of:

1. A versioned `AGENT_CARD.md` schema with YAML frontmatter and Markdown
   narrative.
2. Required identity, purpose, capability, technology, governance,
   memory/data, validation, and limitation sections.
3. A separate evidence manifest containing detailed validation results,
   timestamps, hashes, review data, and proof locations.
4. A schema-conformance validator.
5. Cross-contract consistency checks against the existing template contracts.
6. Mechanical approval-default checks driven by capability verbs.
7. Lifecycle status gates for `disabled`, `standby`, `operational`, and
   `deprecated`.
8. Stale-card and stale-evidence detection.
9. Redaction and forbidden-reference checks.
10. A generic reference card for `agent-template`.
11. A later, separately approved `hve-chief-of-staff` instance as the first
    real-profile conformance test.

The MVP must not add runtime model calls, network publication, external
identity provisioning, registry hosting, or live deployment changes.

## 6. Card contract

The card should contain stable, reviewable metadata including:

- `agent_id`
- display name
- category
- accountable owner role
- profile release version reference
- card schema version
- card revision
- lifecycle status
- declared skills
- capability flags
- tool references
- permission and approval references
- escalation reference
- memory/data reference
- evidence-manifest reference
- decommission reference
- last reviewed date

The machine-readable section must remain small enough for a registry or
orchestrator to load without reading every narrative section.

The human-readable body must cover:

- Purpose and scope.
- Capabilities grouped by verb.
- Technology and prerequisites.
- Governance and approval boundaries.
- Memory and data handling.
- Validation and evidence location.
- Limitations and escalation.

## 7. Resolved design decisions

### 7.1 Ownership

The required card owner is an **accountable owner role**, not a named human.
This models a manager role with direct reports and preserves portability when
the person holding that role changes.

An adapter or deployment registry may resolve the role to a current human or
team. That resolution must not alter the portable card's ownership contract.

Publisher, sponsor, operator, and accountable owner may become separate fields
later if the registry requires them. They must not be conflated in the MVP.

### 7.2 Versioning

The design uses three independent version concepts:

1. **Schema version** — the structure and validation contract.
2. **Profile release version** — the runtime/profile contract summarized.
3. **Card revision** — changes to the card content or references.

A documentation-only correction may increment the card revision without
claiming that the runtime profile changed.

### 7.3 Evidence

Validation status belongs in a separate evidence manifest referenced by the
card. The card should provide a minimal summary and a clear link or relative
reference to detailed proof.

The evidence manifest must record, as applicable:

- Validation command or procedure.
- Pass/fail result.
- Execution timestamp.
- Profile and template versions.
- Relevant source and deployment identifiers.
- Evidence paths or URLs.
- Hashes or equivalent integrity references.
- Reviewer or approver.
- Known gaps and expiry date.

### 7.4 Review freshness

Operational evidence and ownership review expire after **180 days** by default,
matching HVE's twice-yearly formal review cadence.

The 180-day period is a maximum, not a waiver. Changes to identity,
permissions, tools, adapter, model routing, data boundary, deployment, or
external exposure invalidate affected evidence immediately.

### 7.5 Skill verbs and approvals

The skill taxonomy is:

- `knows`
- `recommends`
- `creates`
- `acts`

The validator must enforce these defaults:

- `knows` and `recommends` are advisory by default.
- `creates` and `acts` require approval by default.

Existing machine permission policy remains authoritative. A card cannot grant
an exception. Any exception must be explicit, documented, and approved in the
existing governance path.

### 7.6 External exposure

Future MCP, Phone-a-Friend, or other external exposure must use a separate,
sanitized descriptor. The internal card must not become a public capability
document by adding publication flags alone.

The external projection must exclude internal ownership details, private paths,
approval evidence, memory details, sensitive tool metadata, and deployment
state unless each field is separately approved for publication.

### 7.7 Backfill order

The implementation order is:

1. Define and validate the generic `agent-template` card.
2. Merge and validate the template implementation.
3. Create an `hve-chief-of-staff` card instance as the first real-profile
   conformance test.
4. Evaluate additional profile propagation only after independent review.

This backfill is separate from Alpha Phase E and must not modify the Alpha
repository or live Spark deployment.

## 8. Security, privacy, and governance requirements

The implementation must:

- Never store credentials, tokens, secrets, or raw private memory.
- Reject forbidden cross-profile paths and historical profile fallbacks.
- Reject organization-specific material in generic mode.
- Distinguish declared, approved, enabled, validated, and operational state.
- Treat tools and permissions as references to authoritative manifests.
- Never allow the card to activate a channel or tool.
- Require evidence for status claims.
- Preserve approval provenance and rollback references.
- Fail closed on unsupported schema versions or malformed status evidence.
- Avoid network access and model calls during ordinary validation.
- Preserve the existing auxiliary context minimum of 65,536 tokens.

## 9. Acceptance criteria

### Schema

- A valid generic card parses successfully.
- Missing required fields fail validation.
- Invalid enums, dates, versions, skill verbs, or validation states fail.
- Duplicate skill IDs fail.
- Unsupported schema versions fail closed.

### Cross-contract consistency

- `agent_id` matches `PROFILE.yaml`.
- The card identifies the profile release it summarizes.
- Card tool references resolve to declared tool contracts.
- Permission, approval, escalation, memory, and decommission references resolve.
- Status is compatible with the evidence manifest.
- `creates` and `acts` skills require approval unless an explicit approved
  exception exists.

### Security and isolation

- Secret-like material and credential values are rejected.
- Generic mode contains no HVE-specific identity, private paths, channels,
  credentials, or cross-profile references.
- The card cannot expand permissions or activate external channels.
- Another profile's private runtime roots are rejected.
- External publication fields are absent or disabled in generic mode.

### Lifecycle

- `disabled` permits source-only existence with no runtime.
- `standby` requires health, isolation, and portability evidence.
- `operational` requires all health, isolation, portability, and rollback
  checks to pass, plus current ownership and evidence review.
- `deprecated` requires decommission and rollback references.
- Expired or invalid evidence prevents `operational` status.

### Evidence and provenance

- The evidence manifest records commands, timestamps, versions, proof
  locations, reviewer/approver, known gaps, and expiry.
- Evidence can be traced back to a specific source revision.
- A card cannot claim completion without direct validation evidence.
- Changes to material contracts invalidate affected evidence.

### Portability and rollback

- A clean generic installation validates without an HVE adapter.
- Validation works from a different checkout path.
- Removing the card feature does not alter existing profile permissions,
  memory, service ownership, or runtime behavior.
- Evidence can be rebuilt deterministically.
- No test modifies Alpha or Spark state.

## 10. Production-readiness evidence

Before template implementation is considered ready for propagation, Hermes-coder
must provide:

1. The committed card schema and contract documentation.
2. Passing validation output from a clean generic checkout.
3. Cross-contract consistency results.
4. Security and redaction scan results.
5. Portability evidence from separate installation contexts.
6. Disabled and standby lifecycle evidence.
7. Rollback and decommission evidence.
8. A reviewed generic reference card.
9. A source revision and evidence-manifest reference.
10. A documented limitation list and unresolved compatibility gaps.

The first `hve-chief-of-staff` instance requires a separate review and approval.
Its creation is not implied by approval of this template design.

## 11. Facts, assumptions, and boundaries

### Facts

- `hermes-agent-template` already separates identity, charter, tools,
  permissions, memory, adapters, deployment, validation, and rollback.
- Generic mode is disabled by default and has no organization credentials or
  external channels.
- SQLite/FTS5 is the canonical memory path.
- Auxiliary roles have no tool or memory-write authority.
- The existing auxiliary compression context minimum is 65,536 tokens.
- The current template baseline is `0.6.1`.
- Existing template validation passes at the reviewed baseline.
- The supplied AGENT_CARD specification was a draft and was not implemented.

### Assumptions

- HVE's first audience is internal operators and orchestrators.
- Markdown with machine-readable frontmatter remains suitable for review and
  indexing.
- The card should be useful before a profile is externally callable.
- Local evidence manifests are sufficient for the first implementation.

### Explicit boundaries

- This artifact does not authorize code implementation by itself.
- This artifact does not authorize profile deployment or activation.
- This artifact does not authorize Alpha Phase E execution.
- This artifact does not authorize Spark changes.
- This artifact does not authorize public or third-party agent exposure.
- This artifact does not replace existing profile contracts.

## 12. Implementation handoff

After Hans approves the design and acceptance criteria, implementation may be
delegated to Hermes-coder with a narrowly scoped task in
`humanvalueexchange/hermes-agent-template`.

The implementation task must:

- Use this document as the acceptance baseline.
- Preserve profile isolation and adapter boundaries.
- Preserve the 64K auxiliary-context minimum.
- Add no deployment-instance changes.
- Add no Alpha or Spark changes.
- Include targeted validation and evidence.
- Commit and push the template implementation before any profile propagation.

## Approval record

**Decision:** Approved by Hans Westphal for design artifact and acceptance
criteria development on 2026-09-07.

**Implementation status:** Not yet approved.

**Next gate:** Hans review of this published artifact, followed by an explicit
implementation task for Hermes-coder if accepted.
