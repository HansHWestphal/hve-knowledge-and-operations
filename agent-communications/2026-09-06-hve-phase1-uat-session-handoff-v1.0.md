# HVE Phase 1 GitHub UAT — Session Handoff

**Date:** 2026-09-06  
**Prepared by:** Luna, HVE CTO  
**Status:** Paused cleanly for continuation tomorrow  
**Primary implementation repository:** `humanvalueexchange/hanshermesagent`  
**Governing documentation repository:** `HansHWestphal/hve-knowledge-and-operations`

## Exact stopping point

The previous Phase 1 UAT record was deleted from
`humanvalueexchange/hve-team`. Project 2 has zero items and the prior artifact
trees were removed from `main` with normal deletion commits. Git history was
not rewritten. Phase 0 data and behavior were not changed.

The approved comment-posting implementation is pushed to Hermes:

- Commit: [`80c422f`](https://github.com/humanvalueexchange/hanshermesagent/commit/80c422f)
- Change: approval-gated, idempotent artifact proof comments
- Focused tests at push: 22 passed

Hermes must be restarted or reloaded from that pushed commit before the next
UAT. No new end-to-end task was started after the cleanup.

## What the implementation now does

Phase 1 exposes a named MCP operation:

```text
post_artifact_comment
```

Artifact delivery also invokes the same internal idempotent publisher. The
proof comment uses `[HVE-ARTIFACT <task-id>]` as its reconciliation marker and
contains:

- rendered Markdown link;
- raw file link;
- artifact repository path;
- commit SHA;
- content SHA-256.

The Phase 1 state order is now:

```text
preview
-> explicit Hans approval
-> one issue and one Project item
-> one artifact commit
-> one proof-of-work issue comment
-> Awaiting Validation
-> explicit Hans validation
-> Done
```

If artifact or comment publication fails, the task must be visibly blocked
with its pending action. Validation must verify the proof comment before
allowing `Done`. Phase 0 keeps its original behavior and gates.

## Required fresh UAT

Use a brand-new Hermes session and one harmless Alan- or Brian-owned Markdown
task. Do not reuse a prior task ID or artifact filename from the deleted run.

1. Hermes asks for the explicit owner, deliverable, Five Wealth pillar,
   acceptance criteria, and optional due date/risks.
2. Hermes presents the complete preview and does not create GitHub records.
3. Hans explicitly approves that exact preview.
4. Verify exactly one issue and one Project item.
5. Deliver one harmless Markdown artifact.
6. Verify exactly one artifact commit and exactly one issue proof comment.
7. Confirm the Project item is `Awaiting Validation`.
8. Hans performs separate final validation.
9. Verify the Project item and local task reach `Done`.

Do not delete, rollback, recreate, or validate records during the test unless a
failure is explicitly diagnosed and Hans authorizes recovery.

## Errors to avoid from the previous session

This session lost substantial time because Luna:

- initially treated the absence of Phase 1 MCP tools in the control CLI as a
  runtime readiness failure, even though the prior handoff said the live
  Hermes runtime was ready;
- repeatedly queried stale or incomplete session-store telemetry and used it to
  contradict Hans's direct observation that a live Hermes UAT session was
  running;
- failed to distinguish the control session from the live Hermes WhatsApp
  session;
- described an internal adapter helper as a “comment tool” before registering
  the named MCP operation and updating the Phase 1 tool filter;
- allowed the user to discover the mismatch from Hermes's own message instead
  of checking the exposed MCP contract first;
- changed the implementation before clearly restating the approved plan and
  checkpoint sequence;
- initially left artifact state ordering coupled to local staging, requiring a
  later correction so `awaiting_validation` follows confirmed external proof;
- did not keep the owner discrepancy visible when the first successful record
  was Hans-owned instead of the requested Alan/Brian-owned test.

These are process failures, not user errors. Tomorrow's session must start from
this handoff, verify the pushed commit and active MCP tool filter, and use live
Hermes evidence before making readiness or failure claims.

## Tomorrow's first checkpoint

Before Hermes receives the fresh task, report all of the following:

```text
Pushed commit: 80c422f
Runtime loaded from pushed code: [confirmed / not confirmed]
Phase 1 MCP tools include post_artifact_comment: [confirmed / not confirmed]
Phase 1 DB clean: [confirmed / not confirmed]
hve-team issues and Project 2 items clean: [confirmed / not confirmed]
```

Only after that checkpoint should the new preview be requested.
