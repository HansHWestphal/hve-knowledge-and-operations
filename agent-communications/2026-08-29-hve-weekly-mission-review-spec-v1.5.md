# HVE Weekly Mission Review - v1.5 Contract Amendment

**Date:** August 29, 2026  
**Status:** Draft for CEO review  
**Amends:** `2026-08-29-hve-weekly-mission-review-spec-v1.4.md`

## Decision-ledger integration

The weekly review must consume the governed CEO decision ledger when it exists:

`/home/hans/.hermes/profiles/hanshermesagent/state/weekly-decision-log.jsonl`

The report must reconcile ledger events with report decision IDs and show:

- decisions created during the period
- decisions awaiting Hans's judgment
- active and in-progress decisions
- completed decisions with stated evidence
- deferred, rejected, cancelled, or blocked decisions
- overdue decisions
- changes since the previous report

A decision is not completion evidence by itself. The report must require a
separate outcome, artifact, or verified execution record before counting the
related work as progress.

Decision records must retain source session/message provenance, timestamps,
status history, owner, deadline, linked action or offer slot, and interpretation
confidence. The weekly review must not reproduce unnecessary private speech or
chat content.
