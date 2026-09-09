# HVE Knowledge Architecture Migration — UAT Success Diary

**Date:** 2026-09-01  
**Owner:** Luna, HVE Head Architect and CTO  
**Status:** Approved success record  
**Repositories:** `humanvalueexchange/hve-knowledge-layer`, `humanvalueexchange/hanshermesagent`, `HansHWestphal/hve-knowledge-and-operations`

## Purpose

This diary records the completed HVE knowledge architecture migration validation,
the defects found and corrected, the live user-acceptance sequence, and the
resulting operating state. It is an evidence record, not a policy document and
does not authorize unrelated product, financial, legal, or publication decisions.

## Architecture and ownership

- `hve-knowledge-layer` owns the independent evidence, extraction, chunking,
  LanceDB indexing, validation, and read-only retrieval boundary.
- `hanshermesagent` owns Hermes callers, Telegram intake, Proton intake, worker
  orchestration, and user-facing completion responses.
- HVE-Librarian is the steward and caller; it does not own worker implementation.
- `/hve-library` remains the durable evidence and runtime plane.
- The legacy knowledge-layer source and disabled legacy unit files remain
  intentionally preserved. Full decommission was not claimed.

## Initial migration state

Phase 8 cutover was live before this UAT sequence:

- Replacement native knowledge timers were enabled and active.
- Legacy knowledge timers were disabled and inactive.
- `hve-intake.path` remained enabled and active for manual PDF intake.
- Historical malformed manifests and failure records were preserved.
- `/hve-library` was not deleted, recreated, moved, or automatically repaired.

## Defects found and corrected

### False LanceDB indexing failure

The link collector expected the final stdout line to contain one complete JSON
object. The knowledge-layer CLI emitted pretty-printed multi-line JSON. LanceDB
could successfully write rows while the collector parsed only the final closing
brace and reported `LanceDB indexing failed`.

Correction:

- Added compact machine-readable CLI JSON output.
- Corrected the `index` command exit status to fail unless indexing succeeds.
- Updated the Hermes link collector to request compact JSON.
- Added regression tests for compact success and explicit failure handling.

### Duplicate direct-PDF intake invocation

Direct Telegram PDFs were initially staged in
`/hve-library/intake/inbox`, which is watched by `hve-intake.path`. The Telegram
caller and the manual inbox watcher could therefore invoke the pipeline for the
same file. The shared write lock prevented concurrent mutation, but the caller
could return `SKIPPED reason=another library worker is active` before the watcher
completed the document.

Correction:

- Direct Telegram PDFs now use `/hve-library/intake/telegram`.
- The Telegram PDF collector invokes the public knowledge-layer intake pipeline
  directly.
- Transient shared-lock responses are retried for a bounded period.
- A persistent busy state is returned explicitly rather than as a false indexed
  result.
- Manual PDFs continue to use `/hve-library/intake/inbox` and its watcher.
- Proton intake remains isolated in its private queue and direct worker path.

### Large-document read-back limitation

Large retrieval responses could overflow into a profile spillover cache that
HVE-Librarian could not read with its available tools. Archival and indexing
were successful, but complete curation could not be claimed.

Correction:

- Added the read-only `document_chunks` MCP operation.
- Retrieval is bounded to at most 10 chunks per call.
- Responses include document ID, SHA-256, chunk range, total count, and
  continuation metadata.
- Chunk document identity and SHA-256 are validated before return.
- Paths outside the knowledge-library root are rejected.
- HVE-Librarian memory now directs complete analysis through paginated chunk
  retrieval and prohibits attempts to read local filesystem paths through
  `read_resource`.

## UAT record

### UAT Test 1 — public read-only status boundary

**Result:** Passed.

HVE-Librarian retrieved verified status metrics from the independent public
knowledge-layer boundary. The apparent failure mismatch was reconciled as
explicit historical failure records rather than a current manifest histogram:

- malformed/invalid manifest failures;
- one no-extractable-pages failure;
- historical indexing failures.

No historical failure records were changed.

### UAT Test 2 — direct Telegram PDF

**Result:** Passed.

A controlled Walter Russell PDF completed Telegram capture, caching, intake,
extraction, chunking, LanceDB indexing, manifest finalization, and final
user-facing completion response. The resulting library state advanced from 98
documents / 49 indexed to 100 documents / 51 indexed during that test.

### UAT Test 3 — HTTPS link intake

**Initial result:** Partial/failed end-to-end result caused by the false
LanceDB indexing response.

**Correction:** The compact JSON and exit-code fix was implemented and deployed.

**Final result:** Passed using
`https://growthinreverse.com/ben-meer/`.

The canonical URL, HTTP 200 fetch, Telegram provenance, static HTML extraction,
chunking, LanceDB indexing, manifest finalization, and public retrieval all
completed successfully.

### UAT Test 4 — operational behavior and worker ownership

**Data-plane result:** Passed.

The six malformed historical manifests remained visible and did not prevent
valid processing. The known non-document manifest was skipped rather than sent
through PDF processing.

**Host-level result:** Initially partial because the HVE-Librarian profile had no
systemd, process, filesystem, or log tools. Host verification confirmed the
replacement timers, legacy timer state, active services, and the original
safe-lock behavior. The approved worker ownership correction was then deployed
to remove the duplicate Proton-to-inbox trigger.

### UAT Test 5 — final end-to-end acceptance

**Result:** Passed after the direct Telegram PDF retest.

Controlled workflows completed:

1. **HTTPS link intake**
   - Document ID: `b9f9eb37caa00861`
   - Indexed and retrieved through document and semantic query operations.

2. **Direct Telegram PDF intake**
   - Document ID: `26ffdc9faeea0134`
   - Completed extraction, chunking, indexing, finalization, and retrieval.
   - The first UAT run exposed the duplicate-worker race; the corrected path
     was retested successfully without lock contention.

3. **Proton file intake**
   - Document ID: `4b042ba131bfcb00`
   - Completed queued intake, worker processing, extraction, chunking, indexing,
     finalization, and retrieval through the private Proton worker path.

For the controlled three-workflow run, the evidence showed a baseline of 105
documents / 54 indexed and a final state of 108 documents / 57 indexed.
Failures remained at 10 and the historical error set remained unchanged.

## Large-document retrieval validation

After the UAT Test 5 workflow, a large `$100M Leads` PDF was submitted to
validate the new paginated retrieval boundary.

- Document ID: `6bac7cb3105a43f2`
- Pages: 299
- Chunks: 218
- Manifest: indexed
- LanceDB records: 218
- Pipeline failures: 0
- Pipeline skips: 0

HVE-Librarian retrieved and synthesized the book's extractable framework,
including the Core Four lead channels, Free Goodwill, lead magnets, Open To
Goal, and Lead Getters, without relying on spillover-cache read-back. Its HVE
mapping was explicitly labeled interpretation rather than policy.

## Code and deployment evidence

### `humanvalueexchange/hve-knowledge-layer`

- `915282f` — compact JSON output and corrected index exit handling.
- `0fbbc50` — paginated, provenance-checked `document_chunks` MCP retrieval.

### `humanvalueexchange/hanshermesagent`

- `3f86117` — validated deployment-scoped Proton notification fallback.
- `df8260a` — caller compact-JSON indexing integration and tests.
- `ba8de19` — private Proton staging and direct Proton pipeline ownership.
- `9c0a537` — private Telegram PDF staging, bounded lock retry, and explicit
  pipeline outcome handling.

The active HVE-Librarian gateway was restarted after the profile tool and memory
updates. The active deployment uses `/opt/hve-knowledge-layer/current` and the
approved HVE knowledge-layer MCP boundary.

## Final operating state

- HTTPS link intake: operational.
- Direct Telegram PDF intake: operational with single-owner private staging.
- Proton intake: operational with private staging and direct worker ownership.
- Public document and semantic retrieval: operational.
- Large-document retrieval: operational through bounded pagination.
- Replacement knowledge timers: enabled and active.
- Legacy knowledge timers: disabled and inactive.
- Manual inbox watcher: enabled and active.
- Historical evidence and failure records: preserved.
- No active caller reference to `/home/hans/hermes-v2/scripts/knowledge_layer`
  was found; remaining references are documentation/history only.

## Known non-blocking follow-up

Older Proton job records may retain `processing_status: pending` even when the
authoritative manifest is indexed. This is cosmetic state drift in historical
records and does not invalidate the indexed manifest, archive, or retrieval
result. New worker code updates the processing status after successful intake.

## Decision and closeout

The HVE knowledge architecture migration UAT sequence is recorded as a success.
UAT Test 5 is accepted as **PASS** based on the three completed workflows,
host-level timer/path verification, clean direct-PDF retest, preserved
provenance, successful retrieval, explicit failure handling, and bounded
large-document read-back validation.
