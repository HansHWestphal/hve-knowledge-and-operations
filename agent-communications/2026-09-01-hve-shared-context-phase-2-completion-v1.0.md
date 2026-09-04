# HVE Shared Context and Knowledge-Layer Consumer
## Phase 2 Completion Record

**Date:** 2026-09-01  
**Owner:** Luna, HVE Head Architect and CTO  
**Decision authority:** Hans Westphal  
**Status:** Accepted  
**Scope:** Knowledge-layer consumer boundary and Hermes retrieval behavior

## Outcome

Phase 2 is complete and accepted after implementation, deployment, and a
read-only Hermes WhatsApp acceptance test. The normal Hermes evidence boundary
remains `hve-link-library`; no low-level worker mutation interface was added.

The deployed retrieval path now:

- uses the managed knowledge-layer installation at
  `/opt/hve-knowledge-layer/current`;
- uses Ollama `nomic-embed-text` with the
  `nomic-embed-text-v1.5` 768-dimensional contract;
- reports semantic retrieval, keyword fallback, and backend errors as
  machine-readable fields;
- returns bounded semantic results without raw oversized backend payloads;
- supports metadata-only document chunk pages for provenance and pagination
  checks;
- preserves document IDs, SHA-256 hashes, source paths, manifest paths, chunk
  ranges, validation status, warnings, and continuation metadata;
- prevents Hermes from recovering MCP results through spillover, cache,
  filesystem, shell, SQL, or code-execution tools.

## Repository changes

### `humanvalueexchange/hve-knowledge-layer`

Commits pushed to `main`:

- `1951476` - expose bounded document chunk reads;
- `1447c63` - report knowledge manifest warnings;
- `716b531` - support metadata-only chunk pages.

The public API, CLI, MCP adapter, and contract tests now support bounded
metadata-only chunk retrieval through `include_text=false` (CLI equivalent:
`--metadata-only`).

### `humanvalueexchange/hanshermesagent`

Commits pushed to `main`:

- `5492b57` - keep knowledge metadata inside the MCP boundary;
- `01056d2` - surface knowledge validation warnings;
- `6c37f60` - bound Hermes knowledge MCP responses.

The Hermes adapter now passes the managed subprocess environment, normalizes
semantic result payloads, preserves backend errors, surfaces manifest
provenance and warnings, and uses the bounded chunk contract. The HVE planning
skill explicitly prohibits spillover or filesystem recovery.

## Deployment evidence

- The knowledge layer was installed and systemd units were verified using the
  repository deployment script.
- No independent knowledge-layer timers or new workers were enabled.
- The Hermes gateway was restarted after deployment.
- The gateway, shared-context MCP, and link-library MCP processes were active.
- The knowledge-layer runtime remained rooted at `/hve-library`.
- No runtime state, credentials, or evidence records were committed.

## WhatsApp acceptance test

Hermes session:

```text
20260901_194007_0f65173a
```

The controlled read-only test used only `hve-link-library` MCP responses and
completed without `execute_code`, filesystem, shell, SQL, downloaded-file,
spillover, cache, or mutation tools.

The test demonstrated:

- `retrieval_mode: semantic`;
- `semantic_available: true`;
- `fallback_used: false`;
- `backend_error: null`;
- document `077ca727976752cf`;
- SHA-256 preservation;
- direct source and manifest provenance;
- page 1: chunks `0-9`, `next_start_chunk: 10`;
- page 2: chunks `10-19`, `next_start_chunk: 20`;
- `include_text=false` on both pages;
- non-overlapping continuation;
- direct validation warning propagation.

## Open data-health item

The selected document has a pre-existing contradictory manifest field:

```text
chunk_status: completed
chunk_error: missing extracted_text_path
extracted_text_path: present
index_status: completed
```

The consumer now reports this as a validation warning and does not alter the
evidence record. It must be triaged through the governed knowledge-ingestion
workflow before the document is described as clean. This does not block Phase 2
acceptance because the warning is visible and provenance remains intact.

## Boundary and promotion decision

Phase 2 does not change HVE decision authority, add write paths, or allow source
evidence to override approved decisions. Recommendations remain
non-authoritative, and ledger writes remain approval-gated.

Phase 3 is not started by this record. Promotion requires a separate explicit
approval from Hans.
