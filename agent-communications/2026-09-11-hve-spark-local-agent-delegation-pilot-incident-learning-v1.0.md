# HVE Spark-Local Agent Delegation Pilot Incident Learning

**Date:** 2026-09-11
**Status:** Approved learning record
**Owner:** Luna, HVE CTO / Head Architect
**Decision authority:** Hans Westphal, CEO
**Related issue:** [#21](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/21)
**Related plan:** Spark-Local Agent Delegation Platform Plan v1.1

## Learning: what not to do

The Phase 6 reviewable pilot was not controlled. After the runner exceeded its
initial command wait, it continued in the background without an enforced
whole-cohort deadline, queue-claim deadline, no-progress watchdog, or active
supervision. The runner waited approximately two and a half hours while the
next task remained queued. Hans had to request the stop.

This was an orchestration failure by Luna. A pilot described as controlled must
not depend on passive observation or an open-ended shell process. A per-task
execution timeout alone is insufficient because it does not bound queue wait,
runner wait, or cohort duration.

## Impact

- Phase 6 operating-default readiness was not established.
- The cohort produced no additional qualifying evidence after the first
  corrected task.
- Time was spent without useful progress or an automatic safety decision.
- No production service, production default, unrelated repository change, or
  Issue #19 work was modified.
- The active queued job was cancelled through the supported queue API with an
  explicit reason, and the partial evidence was preserved.

## Required controlled-pilot safeguards

Every future pilot runner must enforce all of the following:

1. A whole-cohort wall-clock budget shorter than the worker execution budget.
2. A queue-claim and worker-start deadline for every submitted task.
3. A no-progress watchdog based on heartbeat and progress evidence.
4. Immediate stop on worker health loss, unexpected concurrency, or routing
   evidence that differs from the assigned workspace.
5. Cancellation through the supported queue API, with an explicit reason.
6. A bounded polling interval and a final status snapshot after cancellation.
7. A fail-closed result when any required evidence is missing.
8. A runner-level maximum task count and stop-on-first-failure policy unless a
   different policy is approved in advance.
9. A preflight check proving that the runner itself has an expiry deadline.
10. A recorded operator, start time, deadline, stop reason, and rollback path.

## Required evidence

A controlled pilot is not complete unless its record includes the cohort ID,
task IDs, workspace paths, queue status transitions, worker health evidence,
telemetry completeness, safety and review results, elapsed wall-clock time,
stop reason, and final evaluation decision.

No local execution default may be broadened from this learning record alone.
The controls must be implemented, tested with temporary databases, and adopted
in the operating plan and SOP before another Phase 6 cohort is attempted.
