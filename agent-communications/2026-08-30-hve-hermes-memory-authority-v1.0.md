# HVE Hermes Memory and Authority Session Note

**Date:** August 30, 2026  
**Status:** Completed session note

## Purpose

Document the session's correction of Hermes memory classification, authority
boundaries, and the stale Bitcoin discount guidance.

## Completed work

### Local SQLite memory classification

- Added explicit authority classes:
  `fact`, `technical_context`, `preference`, `project_context`, `decision`,
  `policy`, and `temporary`.
- Added `authority_class` and `ledger_required` metadata to the profile-local
  SQLite memory database.
- Added schema migration support without rewriting existing source-backed memory.
- Technical context and preferences remain ordinary local memory.
- Explicitly adopted decisions and policies become reviewable candidates with
  `ledger_required=true`; maintenance never writes directly to the weekly
  decision ledger.
- Preserved source quotes, provenance, validation, and dry-run reporting.
- Kept vector-candidate infrastructure disabled.

### Weekly decision ledger boundary

- SQLite is the fast contextual memory and classification layer.
- The governed `hve-decision-ledger` MCP workflow remains the authority layer.
- Persistent chat memory, implementation, recommendations, and “remember this”
  do not create policy or an authoritative decision.
- A ledger entry requires explicit adoption plus owner, approval status,
  effective date, review date, rationale, and provenance.

### Bitcoin discount status

- Retired the stale 80% Bitcoin discount claim from active HVE guidance.
- Bitcoin discount amount and eligibility are currently undetermined.
- Active guidance now prohibits advertising or promising a Bitcoin discount
  until Hans explicitly approves and records the policy.
- Historical communications were preserved.

## Runtime notes

- Restarted the `hanshermesagent` gateway so the updated provider code loaded.
- Confirmed the local database migrated to schema version 3 and passed integrity
  checks.
- Confirmed the explicit approval test classified as `decision` with
  `ledger_required=true`.
- Confirmed no automatic weekly-ledger write or SQLite promotion occurred.
- The local 2B extractor still occasionally violates JSON formatting or omits
  required fields; those outputs remain safely rejected and auditable.

## Files updated in this repository

- `instructions.md`
- `.github/copilot-instructions.md`
- `content-intelligence/programs-brief.md`
- `content-intelligence/copilot-studio-agent-spec.md`

Profile-local Hermes runtime changes remain outside this repository by design.
