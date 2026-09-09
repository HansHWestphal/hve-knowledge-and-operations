# HVE Knowledge Architecture Migration Plan

**Date:** 2026-08-31  
**Owner:** Luna, HVE Head Architect and CTO  
**Status:** Approved direction; implementation not started  
**Decision authority:** Hans Westphal

## Target architecture

```text
humanvalueexchange/hve-knowledge-layer
  Independent evidence and retrieval platform

humanvalueexchange/hve-shared-context
  Independent semantic context kernel

humanvalueexchange/hanshermesagent
  Hermes runtime and agent integrations

hve-librarian profile
  Steward, curator, policy governor, and primary operator

/hve-library
  Durable local evidence, processing, index, and vault data
```

The key rule is that repositories own software, while `/hve-library` owns
durable operational data. No repository should silently become the owner of
another repository's runtime state.

## Phase 0: Freeze and document the boundary

1. Stop treating `hermes-v2/scripts/knowledge_layer` as canonical.
2. Do not commit the current schema patch to `hermes-v2`; port the logic
   instead.
3. Record the architecture decision:
   - `hve-knowledge-layer` owns evidence ingestion and retrieval.
   - `hve-shared-context` owns structured semantic context.
   - `hanshermesagent` owns Hermes runtime behavior.
   - `hve-librarian` governs curation and approvals.
4. Inventory every current caller, systemd unit, timer, script, test, and
   documentation reference.

## Phase 1: Establish `hve-knowledge-layer`

Create:

```text
humanvalueexchange/hve-knowledge-layer
```

Port the mature implementation from:

```text
hanshermesagent/knowledge/layer/
```

The independent repository should own:

- PDF and link intake
- Manifest creation and migration
- Native text extraction and OCR
- Chunking
- Embedding contracts
- LanceDB indexing and querying
- Finalization and rollback
- Provenance and checksum handling
- Document schema validation
- Knowledge-layer systemd units
- Deployment and validation scripts
- Integration tests

Do not copy the obsolete `hermes-v2` implementation as a second competing
version.

## Phase 2: Define stable contracts

Before integrating callers, formalize the interfaces.

### Document manifest contract

Define:

- `manifest_type`
- `document_id`
- `source_path`
- `sha256`
- extraction state
- chunking state
- indexing state
- pipeline version
- schema version

Support a compatibility reader for existing valid manifests so the migration
does not require destructive rewriting.

### Evidence/reference contract

Define how the layer exposes:

- document identity
- canonical source path or URL
- content hash
- title and metadata
- provenance
- trust classification
- processing status

### Runtime API contract

Expose stable commands or Python APIs for:

- ingesting a document
- checking status
- retrieving a manifest
- querying indexed content
- listing failures
- validating the library

The Hermes profile should not import internal implementation modules directly
once the extraction is complete.

## Phase 3: Consolidate the deployment model

Move the following with the independent repository:

- `hve-library-manifest.service`
- `hve-pdf-extract.service`
- `hve-library-chunk.service`
- `hve-library-index.service`
- corresponding timers
- knowledge-layer resource limits
- validation and bootstrap scripts

Repoint deployment from:

```text
/home/hans/hermes-v2/scripts/knowledge_layer
```

to the independent installation.

Prefer systemd units that reference a defined deployment location and virtual
environment rather than an incidental historical checkout path.

The old services should remain available during transition but must not run
both implementations concurrently against `/hve-library`.

## Phase 4: Migrate active callers

Update `hanshermesagent` integrations to consume the independent layer:

- `tools/pdf_collector.py`
- `tools/link_collector.py`
- `knowledge/layer/run_intake_pipeline.py`
- related MCP tools
- profile-specific librarian workflows
- validation scripts and documentation

The `hanshermesagent` repository should retain:

- Hermes runtime logic
- agent tools
- cron jobs
- profile integration
- orchestration
- communication behavior

It should no longer contain the core knowledge-layer implementation.

## Phase 5: Position `hve-shared-context`

Keep:

```text
humanvalueexchange/hve-shared-context
```

as a separate repository and semantic layer.

Initially it should consume the knowledge layer read-only through a filesystem
or API adapter. It should import references, not copy PDFs, extracted text, or
LanceDB data.

Its responsibilities remain:

- canonical HVE entities
- decisions and goals
- append-only events
- trust and permissions
- context packets
- provenance references
- future signed sharing

The adapter must filter `/hve-library` manifests by type and import only valid
evidence references.

## Phase 6: Make HVE-Librarian the steward

The `hve-librarian` profile becomes the primary operator of both systems.

It should:

- request ingestion
- monitor processing status
- review provenance
- curate and classify knowledge
- create governed context updates
- request human approval for sensitive writes
- report completion and failures through Telegram/WhatsApp

It should not own the extraction, OCR, or indexing code.

## Phase 7: Validate before cutover

Required validation:

1. Existing valid PDFs remain discoverable.
2. New PDF intake completes end to end.
3. OCR fallback still works.
4. Link ingestion still works.
5. Manifest migrations preserve hashes and provenance.
6. Non-document manifests are skipped safely.
7. Extraction, chunking, and indexing timers complete successfully.
8. LanceDB queries return expected results.
9. `hve-shared-context` imports references without copying source data.
10. Hermes and hve-librarian can consume the stable interface.
11. Failure states remain explicit and recoverable.
12. No concurrent legacy and new workers mutate `/hve-library`.

## Phase 8: Cutover and decommission

After successful validation:

1. Stop and disable the legacy `hermes-v2` knowledge-layer timers.
2. Enable the independent repository's deployment units.
3. Confirm all active callers use the independent layer.
4. Remove stale `/home/hans/hermes-v2` references.
5. Delete the duplicate knowledge-layer implementation from `hanshermesagent`.
6. Archive the old implementation for provenance if needed, but do not leave it
   deployable.
7. Tag the first independent release and record the deployed version.

## Long-term governance

Each repository should have its own:

- versioning policy
- changelog
- schema compatibility policy
- tests
- release process
- operational runbook
- ownership definition

The most important invariant is:

> The knowledge layer evolves independently, the shared-context kernel
> interprets and governs structured meaning, and HVE-Librarian stewards both
> without becoming the source repository for either.
