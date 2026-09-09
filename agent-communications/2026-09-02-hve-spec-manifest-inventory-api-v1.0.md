# Spec — Bounded Manifest-Inventory API for the HVE Knowledge Library

**Author:** HVE-Librarian (hve-librarian profile)
**Date:** 2026-09-02
**Approver:** Hans Westphal — explicit approval for spec drafting and issue filing, Telegram DM 2026-09-02 ("draft the spec in agent comms and file a github issue for Luna")
**Status:** PROPOSAL — not policy; not a decision. Requires Luna's technical review and Hans's final approval before implementation.
**Target:** `hve-knowledge-library` MCP server (`/hve-library` service)

---

## 1. Problem (verified evidence)

The current `documents` tool exposes only `source_type` and `max_results`. In live use on 2026-09-02:

- A single `documents` call against the 111-document library returned ~430 KB of JSON, forcing spillover-to-disk with no way to page, filter, or project fields.
- The librarian lane's core duties — enumerating what is indexed/failed/invalid, dedup detection, flagging stale material, and filing precise escalation tickets — all require manifest-level views that the current API cannot bound.
- Workaround cost observed: 4 separate calls (`status`, `validate`, `failures`, `documents`) plus manual parsing to answer one curation question that one query should answer.

## 2. Goal

Provide one read-only, bounded, filterable manifest-inventory endpoint on `hve-knowledge-library` so any agent profile can get a precise manifest view (including failure/error context and provenance-field presence) without pulling the full manifest set.

## 3. Requirements

### 3.1 Core endpoint: `list_manifests` (proposed name)

- **Read-only.** No writes, no repair, no mutation of manifests, chunks, or index. Reversible by design (nothing to roll back).
- **Filters (all optional, AND-combined):**
  - `ingest_status`: discovered | archived | indexed | invalid | failed
  - `manifest_type`: document | non_document
  - `book` / `title` substring match
  - `author` substring match
  - `sha256_present`: bool (directly supports the 9 missing-sha256 records)
  - `source_path_exists` (server-side check) — flag-only; the tool must not create, restore, or move files
- **Field projection:** caller selects which fields to return; default minimal set: `document_id, title/book, ingest_status, extraction_status, chunk_status, index_status, sha256_present, source_path_exists, discovered_at, indexed_at`.
- **Pagination:** `offset` + `limit` (max 100 per page) or cursor-based; response must include `total, returned, has_more, next_token`. A full-library call must never require re-fetching all data to see one page.
- **Consistent schema** with existing `documents`/`status`/`failures` output (same field names where they overlap) so downstream tooling is not double-maintained.

### 3.2 Join-on-failure (optional enrichment)

Given `document_id`, inline the last recorded failure record (stage, error, recorded_at) — same data `failures` already returns, joined rather than re-fetched.

### 3.3 Access and privacy

- Local-first; no new network exposure.
- No credential-bearing, private, or restricted content in responses.
- Respect existing MCP auth boundaries of the knowledge-library server; no privilege escalation.

## 4. Non-goals (explicit)

- No host filesystem tools, no terminal, no arbitrary read of `/hve-library` files — those remain out of the hve-librarian profile's authority.
- No manifest repair, re-hashing, or `source_path` restoration in this endpoint (separate ops task, see §7).
- No change to `query` semantic search behavior.
- No new profiles or roles.

## 5. Acceptance criteria

1. `list_manifests` with `ingest_status=invalid` returns only invalid documents with their validation error context, bounded by pagination.
2. `list_manifests` with `sha256_present=false` returns exactly the 9 manifests flagged by current `validate` (as of 2026-09-02), no more, no fewer.
3. Full-library enumeration is possible in ≤ `ceil(N/limit)` bounded pages with `total` reflecting the true count; no spillover-to-disk required for standard curation queries.
4. Response schema is documented in MCP tool metadata and consistent with `documents` field naming.
5. End-to-end verified against the live `/hve-library` library by an automated test that compares against `status` + `validate` + `failures` outputs for parity.
6. Rollback path documented (feature-flag or removal of the tool registration; no data migration involved).

## 6. Verification plan

- Luna/ops runs acceptance checks 1–5 against the live library.
- hve-librarian re-runs the 2026-09-02 curation pass (five-pillar + ops + agentic-infra queries) using only the new endpoint and confirms the 4-call workaround is gone.
- Report results to Hans before any broader rollout.

## 7. Sibling task (tracked separately, NOT in this spec)

- 9 manifests missing `sha256` and 10 manifests whose `source_path` no longer exist (per `validate`, 2026-09-02) — host-side manifest repair / provenance reconciliation. Owner: Luna/ops. File as a separate issue if approved.
- 3 stuck-index chunk sets (HVE Pitch Deck, "The 5 Types of Wealth" intake copy, SHIFT Workbook) from the 2026-08-05 `build_lancedb_index.py` CLI mismatch — re-index once manifests are valid.

## 8. Authority and next steps

- Hans approved this spec drafting and the GitHub issue filing on 2026-09-02.
- Luna reviews for technical feasibility, estimates, and any boundary concerns.
- Hans makes the build/approval decision.
- Nothing here is implemented, committed to, or treated as HVE policy until Hans says so.
