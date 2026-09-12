# HVE Spark-Local Agent Delegation Platform

**Date:** 2026-09-11
**Status:** Approved plan revision with phase outcome annotations
**Owner:** Luna, HVE CTO / Head Architect
**Decision authority:** Hans Westphal, CEO
**Related issue:** [#21](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/21)
**Supersedes:** `2026-09-11-hve-spark-local-agent-delegation-platform-plan-v1.0.md`
**Related operating standard:** Spark Coding Task SOP v1.1

## Objective

Move an increasing share of lower-level agentic work from cloud-hosted agents
to reliable agents running locally on the DGX Spark. The objective is to reduce
recurring cloud cost while preserving safety, quality, supervision,
validation, approval, and auditability.

The target operating model is:

```text
Cloud agents handle exceptional or high-complexity work
        |
Spark-local Hermes agents handle the growing majority of bounded tasks
        |
A local queue provides dispatch, supervision, validation, and evidence
        |
Local models perform work at predictable marginal cost
```

Luna may directly repair Hermes-Coder and Hermes-agent infrastructure when the
delegated coding path itself is unavailable or unsafe. This is a bounded
bootstrap exception. Once the infrastructure is reliable, Hermes-Coder remains
the implementation agent for normal profile, application, and feature work.

## Phase 0: Establish the safe bootstrap baseline

**Owner:** Luna

- Freeze the current Hermes-Coder queue and worker configuration as a known
  baseline.
- Back up the live queue database and record its schema, jobs, reviews, and
  events.
- Create an isolated infrastructure workspace.
- Define host-local ownership and rollback procedures.
- Set explicit time and scope limits for direct Luna infrastructure changes.
- Do not modify existing historical jobs during preparation.

**Exit gate:** The baseline is reproducible, the backup is verified, and the
rollback path is documented.

**Outcome annotation:** **PASS.** The queue, worker, ownership, rollback, and
concurrency baseline was established before infrastructure changes began.

## Phase 1: Add queue lifecycle controls

**Owner:** Luna during bootstrap; Hermes-Coder after bootstrap readiness

Implement and test:

- approval, closure, cancellation, and controlled requeue;
- stale-job classification;
- invalid-transition rejection;
- idempotent lifecycle operations;
- append-only lifecycle events;
- safe recovery of jobs left in claimed or executing states.

**Exit gate:** Copied-database tests prove that historical jobs, reviews, and
events survive lifecycle operations without direct SQL administration.

**Outcome annotation:** **PASS.** Temporary-database validation proved lifecycle
controls, invalid-transition rejection, idempotency, event evidence, and safe
recovery without touching the live queue.

## Phase 2: Harden the worker

Add:

- heartbeat timestamps;
- visible progress states;
- execution timeout enforcement;
- controlled cancellation;
- child-process cleanup;
- worker failure recovery;
- clear distinction between a slow task and a stalled task;
- terminal failure evidence when a task exceeds its budget.

**Exit gate:** A deliberately stalled test worker is detected, stopped,
recorded, and recoverable without leaving an ambiguous claimed job.

**Outcome annotation:** **PASS.** Worker heartbeat, progress, timeout,
cancellation, child cleanup, launch-failure handling, and stale recovery were
implemented and validated with isolated tests and rollback evidence.

## Phase 3: Enforce workspace and safety boundaries

Implement preflight checks for:

- exact repository ownership;
- clean or explicitly isolated workspace;
- allowed and prohibited files;
- branch and baseline commit;
- secret and runtime-state exclusion;
- existing validation commands;
- rollback artifact and owner;
- concurrency conflicts;
- iteration and time budgets.

**Exit gate:** A task cannot enter execution unless it produces
`READY_FOR_DELEGATION`.

**Outcome annotation:** **PASS.** Repository ownership, baseline, branch,
workspace, path, secret/runtime, validation, rollback, budget, and concurrency
contracts were enforced before dispatch.

## Phase 4: Build observability and cost measurement

Record per task:

- success or failure;
- safety and review result;
- wall-clock time;
- human effort;
- turns and tool calls;
- input, output, and cache tokens;
- local model and context;
- cloud fallback usage;
- estimated local and cloud cost;
- retry and recovery count.

**Exit gate:** Local and cloud task performance can be compared using the same
evidence model.

**Outcome annotation:** **PASS.** The metrics schema, cohort identity,
pilot/live classification, strict usage-file parser, model/token/turn/tool-call
capture, telemetry status, and pricing snapshot were implemented. Local Qwen
pricing remains explicitly unknown rather than being represented as a false
priced estimate.

## Phase 5: Establish local-agent readiness

Candidate local-first task classes include:

- bounded code changes;
- focused tests;
- documentation updates;
- repository inspections;
- deterministic maintenance;
- data extraction and transformation;
- report generation.

Escalation triggers include:

- ambiguous ownership;
- destructive or financial action;
- security-sensitive change;
- repeated local failure;
- insufficient context or model capability;
- missing reproducible validation;
- unresolved runtime risk.

**Exit gate:** A task-class matrix identifies work that is local-first,
cloud-escalated, or human-only.

**Outcome annotation:** **PASS.** Readiness policy, task-class routing,
escalation triggers, safety thresholds, pilot identity, and local-first
disposition were established. This does not authorize unrestricted production
defaulting.

## Phase 6: Run a controlled local pilot

**Outcome annotation:** **FAIL — uncontrolled pilot execution.**

The ten-task `phase6-pilot-20260911-r2` cohort met its defined safety,
review, intervention, and recovery thresholds. However, the later reviewable
cohort exposed a workspace-routing defect, and after that defect was corrected,
the runner was allowed to wait approximately two and a half hours without
active supervision or a cohort-level stop condition. The next task remained
queued while the runner continued. The operation was stopped only after Hans
requested it.

This means Phase 6 is **not passed for operating-default readiness**. The
earlier successful cohort remains valid evidence for the controls it measured,
but it cannot compensate for an uncontrolled pilot procedure.

### Required controlled-pilot protocol

Before another Phase 6 cohort is run, implement and test the following:

1. Define a cohort ID, task count, task classes, operator, start time, and
   absolute wall-clock deadline before dispatch.
2. Use fresh isolated workspaces under the approved root and verify the
   effective tool workspace with a routing probe.
3. Run a preflight for every task and refuse dispatch unless the state is
   `READY_FOR_DELEGATION`.
4. Enforce one active worker job unless a separately approved concurrency
   policy exists.
5. Enforce a queue-claim and worker-start deadline for each task.
6. Enforce a per-task execution timeout and a shorter whole-cohort budget.
7. Poll queue state and worker health at a bounded interval.
8. Abort the cohort on a missed heartbeat, unchanged progress beyond the
   no-progress window, unexpected worker exit, workspace divergence, or
   telemetry incompleteness.
9. Stop on the first failed, blocked, misrouted, or review-incomplete task
   unless a different continuation policy is approved in advance.
10. Cancel queued or executing jobs through the supported lifecycle API with an
    explicit reason; never use ad-hoc SQL.
11. Preserve all events, metrics, outputs, failed workspaces, and rollback
    artifacts as evidence.
12. Produce a final status snapshot and evaluate the cohort only after every
    task has a terminal, evidence-complete result.

### Phase 6 evidence requirements

For every task, record the job ID, cohort ID, workspace, status transitions,
worker heartbeat and progress, telemetry completeness, model, token counts,
turns, tool calls, safety result, review result, wall-clock duration, and stop
or recovery evidence. A missing field is a failed evidence gate, not a reason
to infer success.

**Re-entry gate:** A new cohort may run only after the runner-level deadline,
queue-start timeout, no-progress watchdog, fail-closed evaluation, and
operator-stop procedure are implemented and validated with temporary
databases. No local execution default changes until a new controlled cohort
passes all thresholds and Hans approves the operating decision.

## Phase 7: Update the operating SOP

Publish Spark Coding Task SOP v1.2 with:

- the Luna infrastructure bootstrap exception;
- queue lifecycle and recovery requirements;
- worker heartbeat and timeout requirements;
- local-agent readiness gates;
- cloud-escalation rules;
- telemetry requirements;
- stale-job and cancellation procedures;
- controlled-pilot deadlines and watchdogs;
- rollback and decommission controls.

Phase 7 remains pending until the controlled Phase 6 re-entry gate passes.

## Execution order

```text
Baseline and backup
    |
Queue lifecycle controls
    |
Worker timeout and recovery
    |
Workspace and safety enforcement
    |
Telemetry and cost measurement
    |
Controlled local-agent pilot with runner watchdogs
    |
SOP v1.2 adoption
    |
Progressive migration from cloud to Spark-local execution
```

## Current decision boundary

Phases 0 through 5 are complete. Phase 6 is blocked by the uncontrolled pilot
execution and must be re-entered only under the protocol above. Issue #19
remains paused. No production defaults, COS/Librarian/CFO behavior, deployment,
commit, push, or issue closure is authorized by this plan revision alone.

Existing agent capabilities must be preserved throughout migration. No
credentials, runtime state, private data, or unapproved policy may be placed in
this repository.
