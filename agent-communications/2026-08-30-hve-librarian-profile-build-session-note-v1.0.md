# HVE Librarian Profile Build - Session Note

**Date:** August 30, 2026
**Status:** Approved working record
**Owner:** Hans Westphal with Luna

## Purpose

Create and progressively tune the `hve-librarian` Hermes agent profile under
Luna's architecture direction, using the same rigor applied to
`hanshermesagent`, then retire
`hanshermesagentcollector` after the replacement is validated.

The librarian will preserve all approved collector capabilities while expanding
into governed HVE knowledge stewardship, including management of the Obsidian
knowledge layer, archival quality, indexing, retrieval, provenance, and
knowledge-organization workflows.

## Current state

- The `hve-librarian` Hermes profile shell exists at
  `/home/hans/.hermes/profiles/hve-librarian`.
- Its profile description and shell wrapper have been created.
- Its gateway is stopped and no production migration has occurred.
- A first role-specific `SOUL.md` draft has been written for review.
- `hanshermesagentcollector` remains unchanged, active, and authoritative for
  the current Telegram intake workflow.
- No collector capabilities have been retired, redirected, or deleted.

## Planned work

### Profile context

- Review and refine `SOUL.md` for the librarian mandate.
- Create the remaining Markdown context files using the established
  `hanshermesagent` structure where appropriate.
- Separate stable identity and authority from operational configuration,
  transient state, and source-specific instructions.
- Define librarian-specific responsibilities, escalation rules, privacy
  boundaries, provenance requirements, and future-evolution rules.

### Capability migration

- Inventory every capability, MCP server, tool filter, skill, workflow, and
  channel currently used by `hanshermesagentcollector`.
- Recreate the required intake, PDF, URL, transcript, archival, extraction,
  indexing, and retrieval paths for `hve-librarian`.
- Add approved Obsidian HVE knowledge-layer management capabilities.
- Preserve stable identifiers, source context, processing states, error
  reporting, deduplication, and provenance.
- Keep permissions least-privilege and avoid copying unrelated runtime state.

### Validation

- Verify profile identity and instruction precedence.
- Test URL and PDF intake through the configured channels.
- Test archival, extraction, indexing, retrieval, and failure reporting.
- Confirm Obsidian operations are scoped, reversible, and provenance-backed.
- Confirm no unauthorized policy promotion, external publication, or sensitive
  data leakage.
- Compare replacement coverage against the collector capability inventory.

### Collector retirement

Do not retire `hanshermesagentcollector` until all of the following are true:

- `hve-librarian` has passed the agreed capability and safety checks.
- Required channel routing has been redirected and verified.
- Existing collector workflows have a documented replacement.
- Any migration gaps, failed tests, or rollback steps are recorded.
- Hans explicitly approves the retirement.

After approval, pause or remove the collector through the supported Hermes
profile workflow, preserve its historical records, and document the final
retirement evidence.

## Operating boundaries

- `hanshermesagentcollector` remains the live source profile until retirement is
  explicitly approved and completed.
- The librarian does not become Hermes Chief of Staff or absorb CFO, CTO, COO,
  legal, financial, or final decision authority.
- Captured material is not automatically an HVE decision, policy, or endorsed
  position.
- Original sources, context, summaries, classifications, and indexes remain
  distinguishable.
- Destructive, irreversible, privacy-sensitive, external, or authority-changing
  actions require explicit approval and a reversible plan where possible.

## Definition of done

The next profile-build phase is complete when `hve-librarian` is a validated,
documented, capability-complete replacement for the collector, with enhanced
knowledge-layer stewardship, verified routing, a documented rollback path, and
explicit approval to retire `hanshermesagentcollector`.

## Open items

- Finalize the librarian Markdown context set.
- Confirm the complete collector capability inventory.
- Define the Obsidian knowledge-layer operations and permission boundaries.
- Decide channel-routing and cutover sequencing.
- Record validation evidence before requesting retirement approval.
