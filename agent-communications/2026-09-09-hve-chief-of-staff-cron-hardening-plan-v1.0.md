# HVE Chief of Staff Cron Hardening Implementation Plan

**Date:** 2026-09-09  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Draft for Hans review; no implementation authorized  
**Primary backlog issue:** https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/16  
**Related issue:** https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/15

## 1. Objective

Harden the successful Chief of Staff cron migration without changing the
working 03:00 and 06:10 delivery paths. The implementation must make current
health reporting accurate, move the remaining monitoring workload out of the
retired `hanshermesagent` profile, and provide durable evidence when a job is
missed or not delivered.

This document is a proposal only. No runtime, profile, schedule, database, or
service changes should be made until Hans reviews and approves the plan.

## 2. Current evidence

On 2026-09-09, both active Chief of Staff jobs completed successfully:

| Job | Schedule | Result |
|---|---:|---|
| `hve-daily-skill-recommendation-chief-of-staff` | 03:00 EDT | Completed at 03:08:08; delivery recorded as `delivered` |
| `twin-morning-brief-chief-of-staff` | 06:10 EDT | Completed at 06:25:20; delivery recorded as `delivered` |

The active gateway uses `HERMES_PROFILE=hve-chief-of-staff`,
`HERMES_HOME=/home/hans/.hermes/profiles/hve-chief-of-staff`, and
`PYTHONPATH=/home/hans/.hermes/current`.

The morning brief nevertheless reported the prior
`normalize_budget_warning_ratio` failure as an active blocker. This is stale
collector data and must not override the authoritative execution database.

## 3. Scope

### In scope

- Correcting the operational health collector's cron-result source and status
  precedence.
- Completing the watchdog and weekly reliability-review migration described in
  issue #16.
- Preserving historical reliability evidence from the retired profile.
- Adding post-run completion and delivery verification.
- Investigating duplicate-send warnings and documenting the result.
- Representing user-owned x333 curation refusals as expected authorization
  boundaries rather than infrastructure failures.
- Updating UAT evidence and the Chief of Staff runbook.

### Out of scope

- Rewriting the Hermes scheduler.
- Automatically replaying failed jobs.
- Moving or modifying the user-owned x333 skill.
- Changing the successful 03:00 or 06:10 schedules.
- Reactivating the retired `hanshermesagent` gateway.
- Installing new runtime dependencies.

## 4. Implementation phases

### Phase 0 — Baseline and rollback point

1. Record the current active runtime commit, profile paths, job definitions,
   execution database schema, and service state.
2. Snapshot the retired profile's reliability database and watchdog state
   read-only for provenance.
3. Define a migration manifest listing every source path, destination path,
   owner, and verification query.
4. Confirm that no existing successful Chief of Staff cron job is interrupted
   during preparation.

**Gate:** baseline manifest and rollback copies exist; no live behavior changes.

### Phase 1 — Correct health reporting

1. Make the collector read the active
   `/home/hans/.hermes/profiles/hve-chief-of-staff/cron/executions.db`.
2. Define status precedence using durable execution evidence:
   `completed + delivered` is healthy; `completed` without delivery is
   incomplete; `failed`, `unknown`, or missing terminal evidence is actionable.
3. Scope “last failure” to the current job and current reporting window.
4. Mark historical failures as historical after a later successful run.
5. Include the execution ID, scheduled time, terminal status, delivery outcome,
   and evidence path in the collector output.

**Gate:** a controlled fixture proves that yesterday's ImportError does not
   appear as today's active blocker after a successful run.

### Phase 2 — Migrate watchdog and reliability review

1. Move the watchdog script, configuration, schedule, alert state, evidence
   path, and reliability database ownership to `hve-chief-of-staff`.
2. Preserve the retired SQLite history as read-only provenance; do not merge
   records without a migration manifest and duplicate-fingerprint policy.
3. Point the weekly reliability review at the active database.
4. Ensure the watchdog runs under the active Chief of Staff profile and that
   no live schedule references `hanshermesagent`.
5. Keep healthy cycles silent and route only policy-qualified actionable events
   to the intended WhatsApp destination.

**Gate:** reference scan passes; one controlled actionable event is stored and
   routed; one healthy cycle stores no false alert; the weekly review writes a
   durable review record.

### Phase 3 — Add post-run delivery monitoring

1. After each 03:00 and 06:10 job, inspect the execution record.
2. Require both a terminal `completed` state and
   `delivery_outcome=delivered`.
3. Emit a durable monitoring event when either condition is missing.
4. Alert the Chief of Staff channel with the job ID, scheduled time, execution
   ID, failure state, and output path.
5. Do not automatically replay the job.

**Gate:** controlled failed, incomplete-delivery, and successful-delivery
   fixtures produce the correct three outcomes.

### Phase 4 — Investigate duplicate-send warnings

1. Correlate gateway `final-send NOT suppressed` warnings with WhatsApp bridge
   delivery records and execution IDs.
2. Determine whether they represent actual duplicate messages or only a
   conservative diagnostic.
3. If duplicate delivery is confirmed, implement idempotency at the narrowest
   delivery boundary.
4. If no duplicate is confirmed, document the warning as non-blocking and add a
   regression check.

**Gate:** two controlled delivery tests show whether one scheduled execution
   produces one or multiple user-visible messages.

### Phase 5 — Clarify x333 authorization outcomes

1. Preserve the current refusal to autonomously curate user-owned x333 skills.
2. Classify that refusal as an expected authorization boundary.
3. Keep it out of infrastructure-failure alerts.
4. Provide a clear Hans-directed path for an intentional manual skill update.

**Gate:** a curation attempt produces an authorization result, not a false
   watchdog or cron outage.

### Phase 6 — UAT and closeout

1. Observe at least one clean 03:00 and 06:10 cycle after migration.
2. Verify active profile identity, execution completion, delivery outcome,
   collector accuracy, watchdog state, and weekly review evidence.
3. Confirm no live Chief of Staff path references `hanshermesagent`.
4. Update issue #16 with exact evidence paths and commit identifiers.
5. Publish a closeout communication only after Hans approves the result.

## 5. Acceptance criteria

- The current Chief of Staff cron jobs continue to complete and deliver.
- The morning brief reports current cron truth rather than stale historical
  failures.
- Watchdog and weekly reliability review run under `hve-chief-of-staff`.
- Historical reliability records remain queryable without becoming live state.
- Missed, failed, and undelivered jobs create durable evidence and alerts.
- Healthy cycles remain quiet.
- Duplicate-send behavior is understood and either fixed or documented.
- User-owned x333 skills remain protected from autonomous modification.
- No active Chief of Staff dependency remains on `hanshermesagent`.

## 6. Rollback and safety

- Do not restart or reactivate the retired `hanshermesagent` gateway.
- Keep the existing successful Chief of Staff cron definitions unchanged until
  replacement monitoring passes its gates.
- Make database migration additive and reversible; never delete retired
  evidence.
- Stop at the phase gate if a controlled test fails.
- Do not replay production jobs automatically during validation.

## 7. Review decisions requested

Hans review is requested on:

1. The phase order and acceptance gates.
2. The decision to use execution database evidence as the authoritative source
   for cron health.
3. The additive, read-only preservation approach for retired reliability data.
4. The no-automatic-replay rule.
5. The proposed duplicate-send investigation before any delivery change.

Hans Reviewed and approved!
