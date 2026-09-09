# HVE Knowledge Architecture Migration — Phase 7 Validation

**Date:** 2026-08-31
**Owner:** Luna, HVE Head Architect and CTO
**Status:** Complete; Phase 8 approval gate remains separate

## Result

Phase 7 validation was completed without modifying, repairing, deleting,
moving, or reindexing live evidence under `/hve-library`. The independent
knowledge layer is deployed at `/opt/hve-knowledge-layer/current`. Replacement
and legacy systemd timers remain disabled and inactive.

## Delivered

- Added stable public `document` and `documents` operations to
  `hve-knowledge-layer`.
- Added bounded extracted-text retrieval and validated document listing.
- Routed Hermes knowledge-library document reads and recent-link enumeration
  through the independent public knowledge-layer CLI.
- Added the shared non-blocking mutation lock:
  `/hve-library/state/locks/library-write.lock`.
- Applied shared lock coordination to manifest generation, extraction/OCR,
  chunking, LanceDB indexing, link indexing, and intake/finalization.
- Added explicit busy/skip behavior under lock contention.
- Updated knowledge-layer deployment documentation.

## Validation evidence

- Knowledge-layer tests: 19 passed.
- Shared-context tests: 13 passed.
- Hermes client/link tests: 14 passed.
- Isolated real PDF intake passed extraction, chunking, Ollama embeddings,
  LanceDB indexing, finalization, and validation.
- Isolated malformed-PDF handling produced explicit quarantine, failed
  manifest state, failure record, and non-zero status.
- Interrupted-batch rollback and recovery passed.
- Shared-lock contention produced an explicit safe skip.
- Live public interface checks returned valid document references and bounded
  document text without exposing non-document manifests.
- Live LanceDB semantic retrieval returned the expected Layered Money result.
- Native systemd definitions passed verification.

## Live baseline preserved

The live library continues to report 98 document manifests, 1 non-document
manifest, 6 malformed document manifests, and 10 historical failure records.
These findings are pre-existing and were intentionally left untouched.

## Decisions and constraints

- No Phase 8 cutover or decommission action was performed.
- No timer was enabled or started.
- `/hve-library` remains the durable evidence and runtime data plane.
- `hve-shared-context` remains an independent, read-only reference consumer.
- Hermes remains the runtime/integration owner; HVE-Librarian remains steward
  and curator rather than implementation owner.

## Phase 8 entry conditions

Before enabling replacement scheduling or retiring legacy paths, the next
session must obtain Hans's explicit approval for:

1. Coordinating the enabled user intake watcher with replacement workers.
2. Confirming all active callers use the stable knowledge-layer boundary.
3. Stopping and disabling legacy timers.
4. Enabling and validating replacement timers.
5. Removing or archiving duplicate legacy implementation paths.
