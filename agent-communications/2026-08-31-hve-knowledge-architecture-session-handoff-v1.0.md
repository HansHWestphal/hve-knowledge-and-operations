# HVE Knowledge Architecture Session Handoff

**Date:** 2026-08-31  
**From:** Luna, HVE Head Architect and CTO  
**To:** Hans Westphal and the next implementation session  
**Status:** Architecture agreed; implementation pending  
**Primary plan:** `2026-08-31-hve-knowledge-architecture-migration-plan-v1.0.md`

## Decision recorded

Hans agreed with the proposed separation of the HVE knowledge architecture
into independent components.

The knowledge layer should evolve independently from the Hermes agents that
use it. HVE-Librarian will become the operational steward and curator, but it
will not own the knowledge-layer implementation.

The agreed repositories and responsibilities are:

```text
humanvalueexchange/hve-knowledge-layer
  Evidence ingestion and retrieval platform

humanvalueexchange/hve-shared-context
  Agent-neutral semantic context kernel

humanvalueexchange/hanshermesagent
  Hermes runtime and integration clients
```

The durable data plane remains:

```text
/hve-library
```

It must not be treated as a Git working tree or copied into any software
repository.

## Current state at handoff

### Existing implementations

The older implementation is in:

```text
/home/hans/hermes-v2/scripts/knowledge_layer/
```

It is currently referenced by legacy systemd units and was the source of the
recent manifest schema-contract failures.

The richer active implementation is in:

```text
/home/hans/hanshermesagent/knowledge/layer/
```

It includes the current intake orchestration, OCR fallback, finalization,
rollback, embedding contract, indexing, and related tests.

This richer implementation is the source to extract into
`hve-knowledge-layer`. It is not the final permanent home.

### Existing shared-context foundation

The local directory:

```text
/home/hans/hve-shared-context/
```

is an early, uncommitted, agent-neutral context-kernel prototype. It already
contains entity schemas, SQLite storage, append-only events, trust tiers,
permissions, context packets, provenance helpers, filesystem adapters, and
tests.

It is complementary to `hve-knowledge-layer`, not a replacement for it.

### Recent temporary repair

The schema-boundary repair was implemented in the legacy
`hermes-v2` tree only to stop the active timers from crashing. It must not be
treated as the canonical long-term implementation. The logic should be
reapplied or superseded in the extracted independent repository while
preserving the richer `hanshermesagent` functionality.

## Required implementation sequence

The next implementation session must proceed in this order.

### Step 1: Establish repository and ownership

1. Confirm whether `humanvalueexchange/hve-knowledge-layer` already exists.
2. If it does not exist, create it under the HVE organization.
3. Preserve provenance for the source files being extracted.
4. Do not delete or move the deployed trees yet.
5. Establish the repository README, ownership, release, and compatibility
   policy before changing runtime paths.

### Step 2: Extract the mature implementation

Port the implementation from:

```text
/home/hans/hanshermesagent/knowledge/layer/
```

Include the related tests, configuration, deployment templates, bootstrap
logic, and validation scripts that belong specifically to the knowledge layer.

Do not bring Hermes profile prompts, cron behavior, WhatsApp/Telegram logic, or
HVE-Librarian policy into the core repository.

### Step 3: Formalize the document contract

1. Add explicit document manifest typing.
2. Retain backward compatibility for existing valid document manifests.
3. Exclude weekly mission, batch, and other non-document records from PDF
   extraction, chunking, indexing, and evidence-reference imports.
4. Add schema version and pipeline version handling.
5. Make malformed document records fail explicitly without stopping unrelated
   valid documents.

### Step 4: Define the integration boundary

The independent layer must expose stable operations for:

- intake
- status
- manifest retrieval
- failure inspection
- validation
- retrieval/query

Consumers should use the public interface rather than importing internal
modules by filesystem path.

### Step 5: Reconcile deployment

1. Move or recreate the knowledge-layer systemd units in the independent
   repository.
2. Ensure only one implementation can process `/hve-library` at a time.
3. Repoint deployment away from `/home/hans/hermes-v2`.
4. Preserve resource limits, security hardening, and native systemd operation.
5. Keep the service installation native; this DGX environment does not use
   Snap for these services.

### Step 6: Migrate callers

Update `hanshermesagent` and the `hve-librarian` profile to call the
independent knowledge layer. The runtime repository should retain integration
code, not duplicate extraction, chunking, indexing, or manifest logic.

### Step 7: Integrate shared context

Keep `hve-shared-context` independent. Start with a read-only adapter that
imports valid `/hve-library` provenance references without copying source
files. Later, HVE-Librarian can use it for governed decisions, context packets,
curation events, and approval workflows.

The shared-context adapter must not import every JSON file in
`state/manifests/` indiscriminately. It must honor the manifest type contract.

### Step 8: Validate with Hans at each gate

Hans approval is required before each irreversible or externally visible
transition:

1. New repository and ownership model.
2. Initial extracted source tree.
3. Manifest schema and compatibility behavior.
4. New deployment units.
5. First live validation against `/hve-library`.
6. Caller migration.
7. Legacy timer shutdown.
8. Deletion or archival of duplicate implementations.

No production cutover should occur based only on a passing local unit test.

## Acceptance criteria for completion

The migration is complete only when:

- `hve-knowledge-layer` is the sole canonical source for evidence processing.
- `hve-shared-context` remains the sole canonical source for semantic context
  kernel behavior.
- `hanshermesagent` contains no duplicate core knowledge-layer implementation.
- HVE-Librarian operates both systems through stable boundaries.
- All systemd units use the independent knowledge-layer deployment.
- Existing documents retain provenance, hashes, and retrieval behavior.
- New PDF and link intake passes end to end.
- OCR fallback and LanceDB indexing remain functional.
- Non-document manifests no longer crash workers or pollute evidence imports.
- Failure, retry, and recovery states remain observable.
- No legacy `hermes-v2` knowledge-layer timer remains deployable.

## Guardrails

- Do not commit this migration plan or implementation into `hermes-v2`.
- Do not delete current runtime files before the replacement is validated.
- Do not alter or recreate `/hve-library` destructively.
- Do not copy sensitive operational data into Git.
- Do not merge `hve-shared-context` into the knowledge-layer engine merely for
  convenience.
- Do not let HVE-Librarian become a hidden source repository for either core
  platform.

## Immediate next action

Begin with repository discovery and ownership confirmation for
`humanvalueexchange/hve-knowledge-layer`, then prepare the extraction inventory.
No runtime cutover should be attempted in the same step as repository creation.
