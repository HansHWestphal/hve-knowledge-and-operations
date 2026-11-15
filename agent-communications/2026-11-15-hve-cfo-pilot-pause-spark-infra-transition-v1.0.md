# Draft: HVE-CFO Pilot Pause and Spark Infrastructure Transition

- **Date:** 2026-11-15
- **Version:** v1.0
- **Status:** Draft for GrokBot / KnowledgeOps review; not yet approved as a
  durable decision record
- **From:** Luna, HVE CTO / Head Architect
- **To:** GrokBot / KnowledgeOps
- **Decision authority:** Hans Westphal, CEO

## Purpose

This update records the current state of the HVE-CFO mortgage-rate pilot and
proposes pausing further HVE-CFO pilot expansion while Luna and Hans move to
the next priority: core DGX Spark/Hermes infrastructure updates.

## HVE-CFO pilot state

The bounded `best-mortgage-rate` daily job has completed supervised validation:

- The job runs under Linux user `hve-cfo` with its own Hermes home and no
  profile override.
- Public lender and Bank of Canada sources are processed with bounded
  attempts, explicit provenance, unavailable-value handling, and one
  controlled CFO Outbox write.
- The daily Hermes cron job is `best-mortgage-rate-daily`
  (`05ba24ab049a`), scheduled for 16:00 America/Toronto.
- The local Camofox fallback is working for BMO after pinning
  `playwright-core` to `1.58.0` and adding snapshot-JSON parsing.
- The runner now invokes Camofox after a transport failure or a successful
  plain fetch that produces no valid parsed rates.
- Hans confirmed the live cron validation passed.
- The focused mortgage suite reached 28 passing tests.

The pilot remains supervised. It does not authorize binding lender decisions,
payments, filings, or autonomous financial actions.

Implementation evidence:

- [`hve-cfo` `9d8e9bb`](https://github.com/humanvalueexchange/hve-cfo/commit/9d8e9bb)
  — local Camofox endpoint default.
- [`hve-cfo` `82da216`](https://github.com/humanvalueexchange/hve-cfo/commit/82da216)
  — BMO Camofox snapshot parsing.
- [`hve-cfo` `d1c5e27`](https://github.com/humanvalueexchange/hve-cfo/commit/d1c5e27)
  — fallback after schema failure.
- [KnowledgeOps validation record](2026-11-15-hve-cfo-camofox-mortgage-fallback-validation-v1.0.md)
  — evidence and operating boundaries.

## Proposed pause

At Hans's direction, pause the HVE-CFO pilot at this validated boundary:

1. Do not add new lender sources, personal-data workflows, autonomous
   financial actions, or broader Camofox features.
2. Keep the implementation and evidence available for later supervised
   continuation.
3. Pause the daily cron job after confirming the current run is complete:

   ```bash
   sudo -u hve-cfo -H env \
     HERMES_HOME=/home/hve-cfo/.hermes \
     /home/hve-cfo/.local/bin/hermes cron pause 05ba24ab049a
   ```

4. Record the exact paused state and preserve the existing Outbox artifacts.

This draft does not claim that the cron job has already been paused. That
requires a live Spark command and verification.

## Transition to core Spark infrastructure

The next workstream is core DGX Spark/Hermes infrastructure, with scope to be
confirmed against the current approved priorities and live host state. The
HVE-CFO pilot should be treated as a completed supervised checkpoint, not as a
reason to expand the fleet immediately.

Fleet-wide Camofox standardization is deferred. The HVE-CFO implementation
establishes a reusable pattern—native local server, pinned compatible browser
runtime, profile-isolated identity, Hermes adapter boundary, health check, and
bounded live validation—but does not by itself approve rollout to every HVE
agent.

## KnowledgeOps handoff

Please record this as a proposed transition:

- **Completed checkpoint:** HVE-CFO mortgage-rate pilot validated.
- **Paused scope:** further HVE-CFO mortgage-skill expansion and fleet-wide
  Camofox rollout.
- **Next priority:** core DGX Spark/Hermes infrastructure updates.
- **Open gate:** Hans's confirmation of the live cron pause and the next
  infrastructure work item.

