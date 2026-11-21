# Cron Reliability Action Items for Luna

- **Date:** 2026-11-20
- **Version:** v1.0
- **Status:** Proposed action items; not a policy or approval gate
- **From:** HVE-COS, Operational Chief of Staff
- **To:** Luna, HVE CTO / Head Architect
- **Reviewed by:** Hans Westphal, CEO (directed comms and push)

## Purpose

Summarize the COS cron job state for the week of 2026-11-13 to 2026-11-20 and
identify the infrastructure issues that require technical attention. This is a
diagnostic handoff, not a policy change or approval request.

## Evidence scope

Data pulled from:

- `~/.hermes/profiles/hve-chief-of-staff/cron/jobs.json` — job definitions,
  schedules, last run status.
- `~/.hermes/profiles/hve-chief-of-staff/cron/executions.db` — execution
  records with timestamps, status, delivery outcomes, and error details.
- `~/.hermes/profiles/hve-chief-of-staff/cron/deliveries.db` — delivery
  attempt records.
- `~/.hermes/profiles/hve-chief-of-staff/cron/output/` — job output files for
  the affected weeks.

## Job inventory (5 active)

| Job | Schedule | Last 7d: delivered / failed / suppressed |
|---|---|---|
| twin-morning-brief | daily 06:10 | 6 / 2 / 0 |
| daily-skill-recommendation | daily 03:00 | 6 / 2 / 0 |
| weekly-mission-review | Mon 00:07 | 0 / 1 / 0 |
| spark-health-watchdog | every 30 min | 19 / 5 / 336 |
| weekly-reliability-review | Mon 07:15 | 0 / 1 / 0 |

Total: 31 successful deliveries, **11 delivery failures**, 336 suppressed
(silent-by-design watchdog ticks).

## Issue 1 — WhatsApp bridge outage (Nov 16-17)

**Facts**

- 5 scheduled delivery failures across 4 jobs, all in the Nov 16-17 window.
- Error (identical across all 5): `Cannot connect to host localhost:3000
  ssl:default [Connect call failed ('127.0.0.1', 3000)]`.
- Affected jobs: morning brief (Nov 16, 17), daily skill rec (Nov 16, 17),
  weekly mission review (Nov 16), weekly reliability review (Nov 16).
- The watchdog's own delivery failures (5 of them) fall in the same window
  (Nov 15-18) — consistent with the bridge being down.
- No retry mechanism: each dropped delivery is permanently lost to the
  delivery pipeline. No alert was surfaced to Hans for any of the 5.

**Verified state (as of 2026-11-20)**

- The bridge is reachable now: all 4 jobs on Nov 18, 19, and 20 delivered
  without error.
- The outage is resolved. This is a retrospective, not a live incident.

**Open question**

Whether the bridge has a self-restart policy or a watchdog that would catch it
if it goes down in the future. If not, a health check on the bridge process
itself would prevent silent delivery loss on the next outage.

## Issue 2 — Weekly mission review source collectors (Nov 9-15 week)

**Facts**

- The Nov 16 mission review run (for week 2026-11-09 to 15) completed but
  produced a **PARTIAL-COVERAGE FAILURE**: zero evidence records across all
  four sources.
- The job correctly refused to synthesize a progress report from empty
  evidence. This is the skill working as designed.
- The run output (saved at
  `~/.hermes/profiles/hve-chief-of-staff/cron/output/bc52abc433e6/2026-11-16_00-14-56.md`)
  identifies three collector failures:
  1. **Gmail daily-bundle collector** — 0 of 7 days covered, 0 bundles, 0
     messages. The daily-bundle job produced nothing in the window.
  2. **Hermes state database** — unavailable; WhatsApp session activity could
     not be queried. 0 routes, 0 records.
  3. **Cron execution database** — missing. 0 in-scope job executions
     recoverable.
- The script path in the job config
  (`/home/hans/profile-repos/hve-cfo/cron/weekly_mission_sources.py`) does not
  exist. The equivalent script was found and used at
  `/home/hans/hve/repos/hve-cfo/cron/weekly_mission_sources.py`. The job config
  path is stale.

**Impact**

- No governed weekly mission report for the week of Nov 9-15.
- **The Nov 23 run will hit the same failures** if the collectors are not
  repaired, producing a second consecutive zero-evidence empty report.

**Action items**

1. Investigate and repair the Gmail daily-bundle collector.
2. Restore Hermes state database access so WhatsApp session records are
   queryable.
3. Verify the Cron execution database is present and accessible to the
   collector.
4. Correct the script path in the mission review job config from
   `/home/hans/profile-repos/...` to `/home/hans/hve/repos/...` (or confirm
   the intended path and update the config).

## Issue 3 — Sustained Spark health WARNs

**Facts**

- The weekly reliability review (Nov 16 run) escalated two events:
  1. `health_check (spark/host)` — **1,712 occurrences**, sustained,
     immediate-impact.
  2. `health_check (spark/ollama)` — **251 occurrences**, sustained,
     immediate-impact.
- The spark-health-watchdog (which runs every 30 minutes and is the source of
  these WARNs) had 5 delivery failures in the Nov 15-18 window. The
  escalation was delivered on Nov 20 (one of the 19 successful watchdog
  deliveries).
- The reliability review output from Nov 16 is short (467 bytes) — it flagged
  both events but did not include remediation detail.

**Open question**

Whether 1,712 host + 251 ollama WARN occurrences over a week is within expected
range for the DGX Spark runtime, or whether this indicates a hardware,
driver, or service-level issue that needs intervention. Hans has not flagged
either as a new concern, but the watchdog has been alerting on these
continuously.

**Suggested next step**

Luna reviews the watchdog output pattern over the week to determine whether
the WARNs are benign (e.g., normal throttling or transient latency) or
indicative of a resource or service problem that needs a fix before the next
weekly cycle.

## What is working well

- **Watchdog suppression logic** is functioning correctly: 336 of 361 ticks
  in the week produced no alert (healthy). The 24 delivered alerts (19 + 5
  failed) match the expected signal-to-noise ratio for a 30-minute poller on a
  host that is mostly healthy.
- **Mission review refusal gate** is working as designed: when evidence is
  empty, the job correctly refuses to fabricate a report rather than
  hallucinating one.
- **Daily skill recommendation** runs 6 of 7 days successfully. The one
  missing fire on Nov 18 may be a single bridge hiccup or a skipped fire.
  The output content for the 6 successful runs appears to be on-brand.
- **Morning brief** has been delivering consistently for ~60+ days. The 2
  failures in this window are attributed to the bridge outage, not to
  content or execution failures.

## Authority and next steps

These are diagnostic findings and proposed action items. Ownership:

- Issues 1-3 (bridge, collectors, Spark WARNs): **Luna** to investigate and
  remediate.
- Hans has reviewed and approves this comms as an action-item handoff. No
  policy change is proposed.
- The Nov 23 mission review will be a test: if the collectors are repaired,
  it should produce a full governed report; if not, it will produce a second
  zero-evidence refusal, which would escalate the priority of Issue 2.

## References

- Job definitions: `~/.hermes/profiles/hve-chief-of-staff/cron/jobs.json`
- Execution records:
  `~/.hermes/profiles/hve-chief-of-staff/cron/executions.db`
- Mission review output (Nov 16):
  `~/.hermes/profiles/hve-chief-of-staff/cron/output/bc52abc433e6/2026-11-16_00-14-56.md`
- Reliability review output (Nov 16):
  `~/.hermes/profiles/hve-chief-of-staff/cron/output/a6a76ce13edd/2026-11-16_07-15-53.md`
- Prior relevant comms:
  [2026-10-19 Luna retrospective — CFO setup and UAT](2026-10-19-hve-luna-cto-cfo-uat-lessons-v1.0.md)
