# HVE Chief of Staff Fleet Instance Completion Path

**Date:** 2026-09-15  
**Owner:** Luna, HVE head architect and CTO  
**Human approval:** Hans Westphal  
**Status:** Approved execution path  
**Traceability:** HVE knowledge-and-operations issue #40

## Decision

HVE will complete its agent instances in this order:

1. `hve-chief-of-staff`
2. `hve-librarian`
3. `hve-coder-jr`

Each agent must have a complete, template-derived repository, explicit ownership, reproducible deployment provenance, profile-local mutable state, rollback capability, and no hidden dependency on a retired or predecessor codebase.

The first priority is to create the canonical `humanvalueexchange/hve-chief-of-staff` repository from the approved `humanvalueexchange/hermes-agent-template` baseline. This is a source and ownership correction, not a rebuild of the Chief of Staff capabilities that already operate successfully.

## Current Chief of Staff state

The active profile is operational at:

```text
/home/hans/.hermes/profiles/hve-chief-of-staff
```

Existing operational capability includes the Chief of Staff gateway, morning brief, daily skill recommendation, weekly mission review, health watchdog, profile-local memory maintenance, channel configuration, and reliability evidence.

The profile is not yet a complete fleet instance. It has no Git repository, Agent Card, repository-pinned deployment, clean source/runtime boundary, or reproducible rollback lineage. Its approximately 150 MB profile directory contains mixed source, generated configuration, mutable state, caches, locks, credentials, logs, and session artifacts.

The live host also requires explicit boundary reconciliation. In particular, `hermes-proton-worker.service` currently runs from `/home/hans/hanshermesagent`; this is primarily Librarian migration residue, but it prevents the host from being considered fully independent of predecessor codebases.

## Ordered path to completion

### 1. Freeze and classify the current profile

Inventory every Chief of Staff profile file and classify it as repository-owned source, generated configuration, mutable runtime state, secret or credential, historical evidence, or temporary/cache/session data. Do not copy the profile wholesale or delete existing runtime state.

### 2. Bootstrap the canonical repository

Create:

```text
humanvalueexchange/hve-chief-of-staff
```

from the approved template baseline:

```text
37f9f4e4ff5cbfe0d9c1d3e318329ade6c1539e3
```

Add and validate the template-required `AGENT_CARD.md`, `README.md`, `PROFILE.yaml`, `RELEASE.yaml`, `CHARTER.md`, `SOUL.md`, `CONFIG.md`, `PERMISSIONS.md`, `TOOLS.md`, tests, and deployment documentation. Adapt the existing capabilities into this structure without discarding them.

### 3. Define the source/runtime boundary

The repository owns identity, instructions, skills, scripts, configuration templates, cron definitions, watchdog and reliability-review code, deployment manifests, tests, and migration/rollback documentation.

The profile retains mutable databases, locks, logs, caches, credentials, sessions, generated reports, and historical evidence. The repository must document all runtime paths and exclude private or mutable state from source control.

### 4. Establish deployment provenance

Add a deployment mechanism that records the repository URL, source commit, template baseline, deployment timestamp, active profile path, runtime version, and rollback commit. Reconcile the active profile to an exact repository commit without replacing mutable runtime state.

### 5. Remove and classify predecessor references

Audit Chief of Staff source, services, timers, cron definitions, scripts, configuration, deployment paths, maintenance jobs, and channel routing. No active Chief of Staff job, service, script, or configuration may depend on `hanshermesagent`.

Historical references may remain only when explicitly marked as migration provenance. Shared platform dependencies such as the Hermes runtime must be documented separately from predecessor dependencies.

### 6. Add focused validation

Validate from a clean checkout:

- template and Agent Card parsing;
- profile loading;
- no predecessor imports or paths;
- source/runtime separation;
- cron ownership;
- watchdog success and controlled failure;
- weekly reliability review;
- channel configuration;
- memory maintenance;
- rollback to the prior repository commit;
- preservation of existing capabilities.

### 7. Perform controlled activation and observation

Stage the repository-derived profile, run offline and shadow checks, verify one controlled canary, observe gateway, cron, watchdog, memory, and channel behavior, record exact evidence, and promote only after Hans approval. No destructive cleanup or irreversible cutover is implied by this document.

### 8. Continue through the fleet

After Chief of Staff meets its acceptance gates:

1. Reconcile HVE-Librarian against its refactor and provenance issues, including removal of the active Proton dependency on `hanshermesagent`.
2. Reconcile HVE-Coder-Jr against its approved profile definition and shared `hve-coder-runtime` boundary.
3. Record each agent's repository commit, deployed path, runtime owner, state boundary, validation evidence, and rollback reference in issue #40.

## Completion evidence required for Chief of Staff

- Canonical repository URL and initial commit.
- Exact template baseline and repository source revision.
- Validated Agent Card, README, profile metadata, release manifest, and tests.
- Source/runtime classification and excluded-state record.
- Active profile path tied to the repository commit.
- Reference scan showing no active Chief of Staff dependency on `hanshermesagent`.
- Gateway, cron, watchdog, memory-maintenance, channel, and rollback validation results.
- Controlled canary evidence and observation window.
- Human approval for promotion or production cutover.

## Boundaries

- Do not rebuild Chief of Staff from scratch or discard existing capabilities.
- Do not reactivate or modify the retired `hanshermesagent` runtime as a recovery path.
- Do not commit credentials, mutable databases, logs, caches, sessions, or private runtime state.
- Do not perform destructive cleanup or irreversible migration without a separate explicit approval.
- Do not mark Librarian or Coder-Jr complete until the same repository, deployment, state-boundary, predecessor-independence, validation, and rollback evidence exists for each.

## Related records

- Issue #40: Create canonical `hve-chief-of-staff` agent repository and complete fleet instance
- Issue #16: Complete Chief of Staff migration from `hanshermesagent`
- Issue #18: Establish HVE Life OS Ideal State and migrate `hve-chief-of-staff`
- Issue #22: Define `hve-coder-jr`
- Issue #26: Standardize bounded coding delegation to `hve-coder-jr`
- Issue #39: Refactor HVE-Librarian
