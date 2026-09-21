# HVE Chief of Staff Completion Plan

**Date:** 2026-09-20  
**Version:** 1.0  
**Owner:** Luna, HVE CTO / Head Architect  
**Human decision owner:** Hans Westphal  
**Status:** Draft for Hans approval  
**Primary tracker:** [HVE knowledge-and-operations #40](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/40)  
**Canonical repository:** [humanvalueexchange/hve-chief-of-staff](https://github.com/humanvalueexchange/hve-chief-of-staff)

## 1. Purpose

This plan completes the HVE Chief of Staff fleet instance without rebuilding
the working Chief of Staff capability from scratch. It converts the already
validated production behavior into a reproducible, repository-owned,
predecessor-independent, rollback-capable fleet instance and closes the
remaining COS-specific issue work with exact evidence.

The plan deliberately distinguishes four states:

1. **Behaviorally production-grade:** the current Chief of Staff role and
   approval-gated external-write policy are already declared production-grade.
2. **Fleet-instance complete:** source, deployment, mutable state, ownership,
   rollback, and runtime provenance are fully reconciled.
3. **Generic runtime complete:** shared Hermes kernel and updater defects are
   fixed or explicitly accepted as fleet-level exceptions.
4. **LifeOS convergence complete:** the broader HVE Life OS Ideal State and
   controlled architecture migration are approved and validated.

The first two are required to close the Chief of Staff fleet-instance
workstream. The third is a shared-runtime dependency. The fourth is a
separate strategic program and must not be silently represented as complete.

## 2. Current evidence baseline

The following evidence already exists and must be reused rather than repeated:

- Canonical repository:
  `https://github.com/humanvalueexchange/hve-chief-of-staff`
- Template baseline:
  `humanvalueexchange/hermes-agent-template@37f9f4e4ff5cbfe0d9c1d3e318329ade6c1539e3`
- Clean bootstrap and focused validation passed.
- Full Chief of Staff repository suite passed: **167 tests**.
- Step 6 validation passed in commit `95feb87`.
- Step 7 observation/canary passed in commit `8850d0e`.
- Production declaration was approved on 2026-09-15 and published in:
  `2026-09-15-hve-chief-of-staff-production-declaration-v1.0.md`.
- Live profile:
  `/home/hans/.hermes/profiles/hve-chief-of-staff`
- Live gateway:
  `hermes-gateway-hve-chief-of-staff.service`
- Active channel:
  profile-local WhatsApp session
- The current profile-local watchdog and weekly reliability review have been
  migrated and validated.
- The retired `hanshermesagent` and `hermes-v2` paths have no active
  Chief of Staff references in the reconciled configuration, scripts, skills,
  schedules, or systemd units.

The current production declaration explicitly accepts two external findings:

1. The HVE-Librarian collector boundary is handled by the separate Librarian
   migration.
2. The shared Hermes runtime updater remains pinned because it refuses
   automatic promotion when a dependency manifest changes.

These are not COS green checks. They must remain visible as external
dependencies until their owning workstreams close or Hans explicitly accepts
them as permanent operating exceptions.

## 3. Definition of done

Chief of Staff is complete for the current fleet-instance workstream when all
of the following are true:

- `hve-chief-of-staff` is the canonical source and deployment owner.
- The active profile is reproducibly derived from an exact repository commit.
- Mutable state, credentials, sessions, logs, caches, databases, and backups
  remain outside Git and are profile-local.
- No active COS source, schedule, service, script, output path, or channel
  depends on `hanshermesagent`.
- No active COS source or deployment path depends on `hermes-v2` as a
  predecessor runtime.
- The gateway, schedules, watchdog, weekly review, memory maintenance, and
  WhatsApp boundary have current evidence.
- A clean-checkout validation and rollback drill pass.
- The mixed-runtime outage has a permanent prevention rule: stage, validate,
  activate an immutable revision, restart dependent gateways, and record the
  active commit.
- Session-kernel lifecycle behavior is either fixed and tested for COS or
  explicitly classified as a shared-runtime exception with a bounded
  mitigation.
- Issue #40 has a final evidence comment and is closed only after Hans
  approves the closeout.

Full LifeOS convergence, HVE-Librarian completion, and shared-runtime updater
redesign are not silently included in this definition. They remain linked
dependencies with their own owners and approval gates.

## 4. Work packages

### WP-0 — Freeze the baseline and evidence index

**Objective:** prevent rework and preserve the already-approved state.

Actions:

1. Record the current `hve-chief-of-staff` repository commit, live profile
   source revision, gateway unit, active profile path, service state, and
   scheduler inventory.
2. Record the Step 6 and Step 7 evidence paths and their commit identifiers.
3. Snapshot retired-profile evidence read-only; do not delete or rewrite it.
4. Create a migration manifest listing every active COS source, schedule,
   service, state path, output path, dependency, and owner.
5. Classify each item as repository source, generated configuration, mutable
   state, secret, historical evidence, cache, or temporary artifact.

**Gate:** the baseline and migration manifest are complete; no live behavior
changes occur during inventory.

### WP-1 — Finish canonical repository specialization

**Objective:** ensure the repository is a complete COS fleet instance, not
just a clean template bootstrap.

Actions:

1. Verify the Agent Card, profile metadata, release manifest, charter,
   permissions, tools, identity, instructions, tests, and deployment
   documentation identify `hve-chief-of-staff`.
2. Record the preserved capabilities:
   - gateway and interactive WhatsApp operation;
   - daily skill recommendation;
   - twin morning brief;
   - weekly mission review;
   - watchdog and reliability review;
   - profile-local memory maintenance;
   - approval-gated external writes;
   - x333 authorization boundary.
3. Document every capability's source file, schedule, runtime owner, state
   path, test, and rollback behavior.
4. Add a source/runtime boundary check that rejects credentials, databases,
   logs, sessions, caches, generated reports, and host-local state from Git.
5. Add a clean-checkout acceptance command that runs all repository gates.

**Gate:** a clean checkout identifies the COS role, preserves all listed
capabilities, and passes the full suite without private runtime state.

### WP-2 — Make deployment immutable and reversible

**Objective:** prevent another live-checkout/shared-module outage.

Required deployment contract:

1. Fetch an exact approved Git commit into a staging directory.
2. Verify repository identity, commit, release manifest, dependency manifest,
   and expected file checksums.
3. Run the clean-checkout and profile-specific validation suite.
4. Render a deployment manifest containing:
   - repository and commit;
   - template baseline;
   - runtime revision;
   - profile path;
   - deployment timestamp;
   - active service units;
   - rollback commit and prior deployment path.
5. Activate the immutable revision without changing profile-local mutable
   state.
6. Restart only the dependent COS gateway after validation.
7. Verify gateway health, scheduler health, channel health, and memory
   maintenance.
8. Retain the previous known-good revision for immediate rollback.

The updater must never claim that a restart is unnecessary when Python
modules, dependencies, or runtime code changed. If dependency manifests
change, automatic promotion must stop and require explicit validation.

**Gate:** a staged deployment and rollback pass in a temporary or reviewable
path; no production cutover occurs without Hans approval.

### WP-3 — Prove predecessor independence

**Objective:** close the remaining `hanshermesagent`/`hermes-v2` ownership gap.

Actions:

1. Scan repository source, generated service definitions, user units, timers,
   cron definitions, maintenance scripts, environment templates, prompts,
   skills, channel configuration, and output paths.
2. Reject active references to:
   - `/home/hans/hanshermesagent`;
   - `/home/hans/.hermes/profiles/hanshermesagent`;
   - `/home/hans/hermes-v2`;
   - retired service names;
   - predecessor-owned WhatsApp session paths.
3. Permit historical references only in migration evidence and mark them
   read-only provenance.
4. Confirm the WhatsApp session is profile-local and is not a symlink into a
   retired profile.
5. Confirm Proton/Librarian services are outside the COS ownership graph and
   are tracked by the Librarian workstream.
6. Confirm no COS recovery instruction reactivates the retired
   `hanshermesagent` gateway.

**Gate:** a reference scan returns no active predecessor dependency, and the
result is attached to issue #40 with paths and commit identifiers.

### WP-4 — Complete schedule, watchdog, and reliability UAT

**Objective:** convert the already-implemented migration into final closeout
evidence.

Actions:

1. Verify the 03:00 daily skill recommendation and 06:10 morning brief use
   active-profile execution records.
2. Verify terminal status requires both `completed` and
   `delivery_outcome=delivered`.
3. Verify a missed, failed, and undelivered fixture creates durable evidence
   and an actionable alert.
4. Verify a healthy cycle remains silent except for expected evidence.
5. Verify the weekly reliability review reads the active database and writes
   a review ledger entry.
6. Verify historical retired-profile records remain queryable but cannot be
   mistaken for active state.
7. Correlate duplicate-send warnings with delivery records and either fix
   confirmed duplicates or document the warning as non-blocking.
8. Verify x333 refusals remain authorization outcomes rather than false
   infrastructure failures.

**Gate:** one clean scheduled cycle, one controlled failure, one
   incomplete-delivery case, one weekly review, and one authorization-boundary
   case all produce the expected evidence.

### WP-5 — Resolve the session-kernel lifecycle issue

**Objective:** ensure `execute_code` kernels do not remain attached indefinitely
to an inactive COS conversation.

Actions:

1. Reproduce the observed idle-kernel behavior from issue #20 in a controlled
   harness.
2. Define the lifecycle contract:
   - a running cell is never terminated;
   - an attached active session may retain a kernel only when explicitly
     required;
   - completed turns release or schedule deterministic cleanup;
   - gateway shutdown and parent-death cleanup remain safe;
   - cleanup emits observable evidence.
3. Implement the narrowest shared-runtime fix in the owning Hermes runtime
   repository, not in the COS profile as a private workaround.
4. Add focused tests for acquire, reuse, timeout, owner teardown, reset,
   cancellation, gateway shutdown, and parent death.
5. Validate the COS x333 path after the runtime fix and confirm no stale
   kernel remains after the turn boundary.

**Gate:** fix and tests pass, or Hans accepts a documented shared-runtime
   exception with a bounded cleanup schedule and explicit risk.

### WP-6 — Reconcile LifeOS boundaries without blocking current COS operation

**Objective:** keep the strategic LifeOS migration honest while finishing the
   current COS instance.

Actions:

1. Treat issue #18 as the parent architecture decision, not as evidence that
   COS is already migrated onto LifeOS.
2. Resolve the terminology distinction between external LifeOS, HVE Life OS,
   Hermes, and the current COS repository.
3. Update the Ideal State draft with the required security, provenance,
   append-only evidence, authority, privacy, safety, and open-question
   controls identified by review.
4. Do not create a new production LifeOS authority or cut over COS until Hans
   approves the Ideal State and the HVE adapter boundary.
5. Record the current COS repository as the stable production boundary while
   LifeOS work remains in shadow/research status.

**Gate:** either issue #18 receives its own approved migration plan and remains
   open, or its COS-specific dependency is explicitly deferred without
   weakening the current production boundary.

### WP-7 — Final UAT, closeout, and operating handoff

**Objective:** produce a complete, independently reviewable closeout packet.

Required evidence:

- canonical repository URL and exact production commit;
- template baseline and release manifest;
- source/runtime classification;
- predecessor reference scan;
- service and schedule ownership map;
- clean-checkout test output;
- gateway and channel health;
- memory-maintenance evidence;
- watchdog normal and controlled-failure evidence;
- weekly reliability review evidence;
- kernel lifecycle evidence or accepted exception;
- deployment and rollback drill;
- observation-window results;
- open external exceptions with owners and linked issues.

Closeout actions:

1. Publish the final COS completion record in `agent-communications/`.
2. Update issue #16 with the final migration/UAT evidence and close it if all
   acceptance criteria are satisfied.
3. Update issue #14 with the immutable deployment prevention evidence and
   close it when the shared updater/restart contract is verified.
4. Update issue #20 with the kernel result; close only when the generic runtime
   acceptance criteria pass.
5. Update issue #40 with the complete evidence index.
6. Close #40 only after Hans reviews the packet and explicitly approves
   closure.

## 5. Issue disposition

| Issue | Disposition in this plan |
|---|---|
| #14 mixed-runtime outage | Close after WP-2 proves staged immutable deployment and restart-required behavior. |
| #16 COS migration | Close after WP-3 and WP-4 prove sole active ownership and UAT. |
| #18 LifeOS convergence | Keep open as a separately approved architecture program; do not falsely close it as part of current COS completion. |
| #20 session kernel | Resolve in the shared runtime or record a Hans-approved bounded exception. |
| #27–#29 cron/COS controls | Close or link to evidence after WP-4 confirms the migrated control plane; avoid duplicate implementation. |
| #37 fleet self-evolution | Keep open as fleet-wide governance; COS completion must remain compatible with it. |
| #40 canonical COS fleet instance | Primary closeout issue; close last. |

External dependencies:

- HVE-Librarian collector ownership remains under the completed Librarian
  migration and must not be silently absorbed into COS.
- Shared Hermes runtime updater changes remain a fleet infrastructure item.
- The CFO rebuild is tracked in
  `humanvalueexchange/hve-cfo#2` and is not a COS dependency.

## 6. Rollback and failure policy

- No destructive cleanup of retired profiles, historical evidence, databases,
  sessions, or backups.
- No automatic replay of missed production jobs.
- No reactivation of `hanshermesagent` or `hermes-v2` as a recovery path.
- Stop at the first failed phase gate and preserve evidence.
- Roll back to the last known-good repository revision, not by editing the
  live checkout in place.
- Do not restart unrelated services or modify Librarian, CFO, Coder, Ollama,
  vLLM, or production queues.
- Do not claim COS completion from a plausible local state; every acceptance
  claim requires an exact artifact, commit, runtime, or execution record.

## 7. Draft agent communication

### To HVE-COS

> **Subject:** COS completion execution boundary
>
> HVE-COS remains the accountable operational owner of its profile-local
> schedules, watchdog, reliability database, memory maintenance, channel
> boundary, and approval-gated external writes. Do not use
> `hanshermesagent` or `hermes-v2` as a recovery path. Do not delete or
> rewrite historical evidence. Report each scheduled execution with terminal
> status, delivery outcome, execution ID, source commit, and evidence path.
> Treat x333 curation refusal as an authorization boundary, not an outage.
> Stop and escalate on an unknown runtime commit, predecessor dependency,
> missing delivery evidence, duplicate delivery, or stale kernel.

### To HVE-Coder-Jr

> **Subject:** Bounded implementation ownership for COS completion
>
> Implement only narrowly scoped, approved changes in the owning repository.
> First priority is the immutable deployment/release contract and its focused
> tests; second priority is the shared session-kernel lifecycle fix only if
> assigned to the correct Hermes runtime repository. Do not modify live COS
> state, restart production services, delete predecessor evidence, or broaden
> into LifeOS migration. Every change must include a reproducible validation
> command, rollback reference, and exact commit evidence.

### To HVE-Librarian

> **Subject:** COS boundary and Librarian independence
>
> Continue owning the Librarian collector and evidence-plane migration under
> its repository and issue records. Do not move the Proton collector into COS
> to make the COS reference scan appear clean. Report the active collector,
> repository commit, service owner, and any host-level finding that remains
> external to COS. Preserve historical evidence and use the approved
> provenance contract.

### To HVE-CFO

> **Subject:** COS completion boundary
>
> CFO rebuild work remains in `hve-cfo` and must not be coupled to COS
> completion. Preserve the CFO capability inventory, offline/rebuild gate,
> read-only-first finance controls, and human approval boundary. Report only
> through the canonical CFO issue and repository.

## 8. Approval requested

Hans approval is requested for:

1. This phase order and definition of done.
2. Closing COS-specific issues only after exact evidence is attached.
3. Treating LifeOS convergence as a separate open architecture program.
4. Fixing the session kernel in the shared runtime rather than adding a COS
   private workaround.
5. The no-destructive-cleanup, no-automatic-replay, and no-predecessor-
   recovery rules.

Until this approval is recorded, this document is a plan only. No live
service, profile, schedule, database, channel, or runtime state is authorized
to change because this plan exists.
