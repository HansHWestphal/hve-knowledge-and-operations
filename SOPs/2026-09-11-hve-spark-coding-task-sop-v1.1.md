# HVE Spark Coding Task SOP

**Owner:** Luna, HVE CTO / Head Architect
**Decision authority:** Hans Westphal, CEO
**Date:** 2026-09-11
**Version:** 1.1
**Status:** Adopted
**Effective:** 2026-09-11
**Supersedes:** v1.0 upon adoption
**Scope:** Coding and code-adjacent implementation work executed on the DGX Spark

## 1. Purpose

This SOP defines the repeatable control loop for coding work performed on the
Spark. It separates implementation from supervision, keeps repository
ownership explicit, makes validation evidence reproducible, and prevents a
plausible local result from being reported as an approved or deployed change.

The default operating model is:

```text
Hans defines or approves intent
        ↓
Luna diagnoses, scopes, delegates, monitors, and validates
        ↓
Hermes-Coder edits, tests, and reports
        ↓
Luna reviews evidence and diff
        ↓
Hans approves material commit, push, merge, or deployment actions
```

## 2. Authority and boundaries

- **Hans** owns product intent, scope approval, material risk acceptance,
  final validation, and approval for commit, push, merge, or production
  deployment unless a narrower authority is explicitly recorded.
- **Luna** owns technical diagnosis, task decomposition, repository selection,
  worker supervision, evidence review, acceptance recommendation, and
  escalation.
- **Hermes-Coder** owns bounded implementation work in its assigned workspace.
  It may inspect, edit, and run approved validation commands, then report
  results. It must not infer scope, commit, push, merge, deploy, or change
  unrelated files.
- **GitHub** is the system of record for approved durable artifacts. Runtime
  changes belong in their owning Hermes or application repository, not in the
  HVE knowledge-and-operations repository.

No task is considered shipped because a worker reports success. It is shipped
only after the required approval, repository, and deployment evidence exists.

## 3. Task intake and contract

Before delegation, Luna records a bounded task contract containing:

| Field | Required content |
|---|---|
| Task ID | Stable identifier used in queue, logs, commits, and reports |
| Objective | One measurable outcome |
| Target repository | Exact repository and branch or release lineage |
| Workspace | Fresh or explicitly verified clean checkout path |
| Allowed files | Files or directories Hermes-Coder may modify |
| Prohibited actions | Commit, push, deployment, dependency changes, or other exclusions |
| Acceptance criteria | Observable behavior and required tests |
| Validation commands | Existing, named commands only |
| Iteration budget | Maximum implementation/revision attempts |
| Risk and rollback | Data, service, compatibility, and rollback considerations |
| Evidence required | Diff, test output, status, review, and deployment proof where applicable |

Ambiguous scope, missing repository ownership, unavailable tests, or a
potentially destructive action is a stop-and-escalate condition.

## 4. Preflight gate

Luna must complete and record the following before Hermes-Coder edits:

1. Read the target repository's current instructions and applicable operating
   plan or decision record.
2. Confirm the target repository is not a retired, unrelated, or wrong-profile
   repository.
3. Identify the authoritative source for every file that may change. A
   host-local file, deployment symlink, generated file, or candidate checkout is
   not an owning repository until that ownership is proven.
4. Create or select an isolated workspace under the approved Spark workspace
   root.
5. Confirm the workspace is fresh or clean and based on the intended branch or
   commit. Never overwrite, reset, stash, or discard unknown user changes.
6. Record the baseline commit, branch, status, and relevant runtime/profile
   version.
7. Confirm the named validation commands exist.
8. Confirm the task does not overlap an active worker, scheduler, deployment, or
   live UAT session without an explicit concurrency decision.
9. Confirm secrets, credentials, private data, and runtime state are excluded
   from the workspace and evidence.
10. Confirm rollback ownership, rollback artifacts, and the recovery procedure
    before any runtime or deployment change.

For disposable smoke tests, the workspace must have its own Git baseline so
the review hook can inspect the intended diff. A parent-repository ignore rule
is not sufficient evidence of an isolated reviewable change.

## 5. Mandatory safe-pause protocol

Preflight produces one of two states:

```text
READY_FOR_DELEGATION
BLOCKED_PENDING_RESOLUTION
```

Luna must select `BLOCKED_PENDING_RESOLUTION` and stop before queue submission,
editing, service restart, deployment, cleanup, or issue closure if any of the
following is true:

- A live kernel, profile, gateway task, scheduler run, UAT, or deployment is
  active and its purpose, owner, or validation status cannot be safely
  established.
- The proposed target file or wrapper contains an uncommitted user change.
- The authoritative owning repository, branch, or release lineage is unknown.
- A host-local file or systemd unit has no confirmed owner and no approved
  change path.
- The known-good release, rollback artifact, or recovery procedure cannot be
  identified.
- The workspace, runtime, or external task state is inconsistent or
  contradictory.

When blocked, Luna must:

1. Make no code edits and submit no Hermes-Coder job.
2. Not restart, resume, terminate, delete, stash, reset, overwrite, or clean
   up anything.
3. Record the exact blocker, evidence source, timestamp, affected task or file,
   and the decision required to proceed.
4. Preserve the live task and user changes unchanged.
5. Report the work as **blocked before implementation**, not failed or complete.
6. Identify the smallest resolution needed for each blocker and its owner.
7. Create a fresh bounded continuation task only after the blockers are
   resolved; do not resume from inference.

### 5.1 Live-task evidence requirement

For an active task, record its exact profile, task or execution ID, process or
gateway identity, start time, current state, owner, and UAT/approval state.
If the purpose or UAT status is not directly observable, treat it as unknown.
Only Hans or an explicitly authorized runtime owner may resolve that ambiguity.

### 5.2 Dirty-file preservation requirement

When a target file or wrapper has user modifications, record its path,
repository/remote if known, status, and non-destructive diff summary. Do not
overwrite, reset, stash, or amend those changes. Implementation requires the
user change to be explicitly preserved, incorporated, or removed by its owner.

### 5.3 Ownership and host-local files

Repository ownership must be proven through authoritative metadata such as the
remote, deployment manifest, package source, or documented release process.
Candidate repositories, unrelated checkouts, and dirty directories are not
substitutes. A host-local deployment helper or systemd unit may be changed only
after Hans authorizes the host-local change path and the task contract records
how the change will be backed up, validated, and rolled back.

### 5.4 Resume gate

Work may resume only when Luna records:

- live-task purpose, owner, and UAT state;
- a safe, explicit disposition for every dirty user change;
- authoritative repository and branch ownership;
- clean or intentionally isolated implementation workspace;
- known-good release and rollback procedure;
- no conflicting worker, deployment, or UAT activity;
- Hans's approval where the resolution changes scope or risk.

## 6. Delegation and monitoring loop

Luna submits one narrowly scoped task to the actual Hermes-Coder queue only
after `READY_FOR_DELEGATION`. The delegation prompt must repeat the task
contract, workspace, allowed scope, prohibited actions, validation command,
iteration budget, and required report.

Luna monitors the queue and worker rather than editing the same scope in
parallel. The normal state progression is:

```text
queued → claimed → completed → reviewed → awaiting_approval
```

The worker may enter `failed`, `needs_revision`, or another non-terminal state.
Luna must capture the state transition, timestamps, iteration count, worker
error, and any review result. A successful file edit without a terminal queue
record is incomplete.

### Stop conditions

Luna stops the worker loop and escalates when:

- the worker exceeds its iteration or time budget;
- the task scope expands or the target repository changes;
- tests are unavailable, contradictory, or unexpectedly broad;
- the worker touches prohibited files or performs a prohibited action;
- a service, data, security, or compatibility risk appears;
- the worker reports success without reproducible evidence;
- the worker and review evidence disagree.

Retries must be new, explicit bounded instructions. Do not silently requeue an
ambiguous or potentially destructive task.

## 7. Validation and review gates

Hermes-Coder must report:

- files changed and files intentionally not changed;
- exact commands run and their complete result;
- failures, skips, warnings, and environment limitations;
- remaining risks and unresolved items;
- whether commit, push, deployment, or external publication was performed.

Luna independently verifies, from the correct workspace:

1. The queue reached a terminal/reviewable state.
2. The diff contains only in-scope changes.
3. `git diff --check` passes.
4. The named targeted tests pass; broader tests are run only when required by
   the repository contract or when targeted results justify escalation.
5. The implementation satisfies each acceptance criterion.
6. The built-in read-only Luna review is present and returns `PASS`, or any
   `REVISE` findings are resolved in a bounded follow-up loop.
7. The target repository status and branch lineage remain understood.

For runtime work, validation additionally covers service health, configuration,
logs, rollback state, and the relevant watcher or UAT evidence. Internal helper
capability must not be described as an exposed tool or as deployed behavior
without direct registration and runtime proof.

## 8. Approval, commit, and delivery

After validation, Luna provides Hans a concise acceptance packet containing:

- task ID and target repository;
- before/after commit or branch identity;
- changed-file summary;
- acceptance criteria result;
- test and review evidence;
- risks, rollback path, and any deviations;
- exact next action requiring approval.

Until Hans approves the applicable gate, Hermes-Coder must not commit, push,
merge, publish, or deploy. After approval:

1. Luna or the explicitly authorized operator creates the commit using the
   repository convention and required Copilot co-author trailer.
2. The approved commit is pushed to the owning GitHub repository.
3. A pull request, issue comment, or durable artifact links the evidence.
4. CI, review, merge, and deployment gates are verified independently.
5. The final status records exact commit, PR/issue, deployment, and validation
   identifiers. A failed push or deployment is reported as failed.

No draft, transient note, credential, runtime state, or unapproved policy is
committed to the HVE knowledge repository.

## 9. Runtime and deployment safety

For changes affecting Hermes, schedulers, services, models, or live data:

- schedule changes away from conflicting jobs before implementation;
- use an explicit lock where concurrent execution is possible;
- preserve restart stderr and actionable failure context;
- verify each service individually after activation;
- retain a known-good release and test rollback before declaring success;
- do not restart or clean up a live task based on inference;
- obtain explicit approval before destructive cleanup or final production UAT;
- close the task only after runtime, scheduler, delivery, and watcher evidence
  agree.

The SOP does not authorize changes to the incident tracked in
`HansHWestphal/hve-knowledge-and-operations#19`; that work remains a separate,
explicitly approved implementation task.

## 10. Evidence record

Each completed or safely paused task must leave an auditable record containing,
as applicable:

- task contract and approval reference;
- preflight state: `READY_FOR_DELEGATION` or
  `BLOCKED_PENDING_RESOLUTION`;
- queue job ID, worker state transitions, and iteration count;
- baseline and final repository identifiers;
- changed-file list and review result;
- exact validation commands and outcomes;
- issue, pull request, commit, and deployment URLs or identifiers;
- runtime health and rollback evidence;
- unresolved blockers, risks, and owners;
- final Hans approval, rejection, or explicit pause decision.

The record must distinguish **observed fact**, **worker report**, **Luna
assessment**, **Hans approval**, **deployment proof**, **blocked condition**, and
**open risk**.

## 11. Standard completion or pause report

```text
Task:
Task ID:
Target repository / branch:
Preflight state:
Worker job:
Baseline commit:
Final diff:

Acceptance criteria:
- [ ] ...

Commands and results:
- `...` — PASS/FAIL/NOT RUN (reason)

Hermes-Coder result:
Luna review:
Files changed:
Live-task conflicts:
Dirty user changes:
Ownership findings:
Rollback evidence:
Risks / unresolved items:
Commit / push / PR:
Deployment / UAT:
Hans approval or pause decision:
Final status:
```

## 12. SOP change control

This v1.1 revision is adopted by Hans Westphal effective 2026-09-11 and
supersedes v1.0. Changes to authority, approval gates, repository boundaries,
worker permissions, deployment safety, safe-pause requirements, or evidence
requirements require a new version and an explicit decision record.
Implementation experience may produce minor clarifications, but no
clarification may weaken a safety or approval gate without recorded approval.
