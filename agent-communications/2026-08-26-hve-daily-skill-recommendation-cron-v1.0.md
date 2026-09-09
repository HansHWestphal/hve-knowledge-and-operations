# HVE Daily Skill Recommendation Cron Fix

**Date:** 2026-08-26
**Owner:** Hermes-coder

## Issue

The `hve-daily-skill-recommendation` Hermes cron job
(`c6895f6b9552`) was reaching the HVE link-library MCP server with malformed
arguments to `read_link_document`. The tool rejected the document IDs, and
Hermes retried the same failing call until the `same_tool_failure_halt`
guardrail stopped the run. The job was marked successful only because the
guardrail response was still delivered to WhatsApp, not because the intended
recommendation workflow completed.

## Fix

The job prompt was updated to:

- Require the exact lowercase 16-character hexadecimal `document_id` returned
  by `list_recent_links`.
- Reject titles, URLs, paths, objects, placeholders, and guessed IDs.
- Allow at most one document read per item.
- Stop using `read_link_document` after any error instead of retrying.
- Treat `search_link_library` results as snippets unless an exact ID is
  available.
- Continue with fresh web research when link-library context is empty or
  unavailable.

The Hermes gateway was restarted to load the updated profile configuration.

## Verification

The job was manually triggered after the first guardrail update and completed
with a valid WhatsApp recommendation rather than a guardrail halt. The final
prompt tightening was then applied and the gateway was reloaded successfully.
The next scheduled run remains 03:00 America/Toronto.

The Hermes profile configuration is maintained outside this repository; this
record documents the operational issue and resolution.
