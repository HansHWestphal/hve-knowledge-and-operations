# HVE Spark-Local Agent Delegation Platform

**Date:** 2026-09-11  
**Status:** Approved implementation plan  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Related issue:** [#21](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/21)  
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

## Phase 6: Run a controlled local pilot

Use low-risk task classes and measure:

- completion and review pass rate;
- intervention rate;
- average latency;
- token consumption;
- cost per successful task;
- recovery frequency;
- cloud escalation frequency;
- human acceptance effort.

**Exit gate:** Local execution becomes the default only for task classes
meeting predefined safety, quality, and efficiency thresholds.

## Phase 7: Update the operating SOP

Publish Spark Coding Task SOP v1.2 with:

- the Luna infrastructure bootstrap exception;
- queue lifecycle and recovery requirements;
- worker heartbeat and timeout requirements;
- local-agent readiness gates;
- cloud-escalation rules;
- telemetry requirements;
- stale-job and cancellation procedures;
- rollback and decommission controls.

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
Local-agent pilot
    |
SOP v1.2 adoption
    |
Progressive migration from cloud to Spark-local execution
```

## First implementation milestone

Luna will repair and validate the queue lifecycle and worker recovery
infrastructure in isolation. No issue #19 implementation or broad task
migration begins until that milestone passes its acceptance gate.

Existing agent capabilities must be preserved throughout migration. No
credentials, runtime state, private data, or unapproved policy may be placed in
this repository.
