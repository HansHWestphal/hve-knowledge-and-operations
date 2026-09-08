# HVE Hermes Self-Improvement Fleet Protocol

**Date:** 2026-09-08  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Proposal for implementation  
**Scope:** Safe Hermes self-improvement and fleet-wide release awareness  
**Backlog issue:** https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/15

## 1. Objective

Hermes should retain its intended ability to improve itself while preventing
experimental, incomplete, or partially validated runtime changes from silently
becoming fleet-wide production code.

The core rule is:

> Self-improvement may produce candidates freely; only the deployment manager
> may promote runtime code into the active release.

## 2. Change classes

### Profile-local skill changes

Changes to a profile-local skill, such as the Chief of Staff x333 skill, remain
inside the owning profile. They do not change the shared Hermes runtime and do
not require a fleet restart.

They must still respect the skill's authorization, provenance, approval, and
publication rules.

### Hermes runtime changes

Changes to Hermes Python code, gateway behavior, cron behavior, or shared
dependencies must be produced in a candidate branch or worktree. The active
runtime must never be edited directly.

### Material or dependency changes

Dependency, security, profile-contract, architecture, and material behavior
changes stop at `awaiting_approval` for Hans review.

Routine runtime changes with unchanged dependencies may promote automatically
after the standard validation gate passes.

## 3. Fleet awareness contract

Agent prompts and memory are informative but are not the enforcement boundary.
The fleet needs a shared, durable, machine-readable release contract.

### Canonical policy

The HVE operations repository should contain the human-readable policy and
implementation record. The local host should carry a synchronized machine-
readable copy:

```text
/home/hans/.hermes/runtime-policy.json
```

### Read-only deployment state

Every profile should be able to read the active deployment state, including:

```json
{
  "active_commit": "<github-commit-sha>",
  "release_state": "known_good",
  "previous_known_good": "<github-commit-sha>",
  "validation": "passed",
  "profiles": [
    "hve-chief-of-staff",
    "hve-librarian",
    "hermes-coder"
  ],
  "updated_at": "<timestamp>"
}
```

The state must distinguish `candidate_created`,
`awaiting_approval`, `known_good`, `activation_failed`, and
`rolled_back`.

### Durable lifecycle events

The deployment manager should emit:

- `runtime.candidate_created`;
- `runtime.validation_passed`;
- `runtime.activation_started`;
- `runtime.activation_succeeded`;
- `runtime.activation_rolled_back`;
- `runtime.awaiting_approval`.

Online agents may receive the event immediately. Offline agents must read the
latest state when they start. No profile should rely on a chat message or stale
context window to learn which runtime is active.

## 4. Safe self-improvement flow

```text
Self-improvement idea
        |
        v
Candidate branch or worktree
        |
        v
Tests and deployment validation
        |
        +--> routine change: automatic promotion
        |
        +--> material/dependency/security change: Hans approval
        |
        v
Immutable active release
        |
        v
Fleet lifecycle event and deployment record
```

If validation or startup fails, the deployment manager keeps the prior release
active or rolls back to the previous known-good release. Profile-local memory,
cron state, workspaces, logs, and skills are never rewound with runtime code.

## 5. Implementation roadmap

1. Define the canonical policy and lifecycle-event schema.
2. Add deployment-manager status and event records.
3. Route Hermes self-improvement promotion through the deployment manager.
4. Enforce that profile-local skill updates cannot mutate shared runtime code.
5. Add approval, validation, rollback, and fleet-state smoke checks.
6. Validate Chief of Staff, Librarian, and Hermes-Coder through UAT.

## 6. Acceptance criteria

- A self-improvement candidate cannot modify the active runtime directly.
- Every activation identifies an exact GitHub commit.
- Every active profile can read the current release state.
- Material and dependency changes stop at approval.
- Failed activation produces a durable rollback event and restores the prior
  known-good runtime.
- Offline profiles converge on the latest state at startup.
- Existing Chief of Staff, Librarian, and Hermes-Coder UAT paths remain
  operational.

## 7. Provenance

- Outage issue:
  https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/14
- Runtime release safety proposal:
  https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-08-hve-hermes-runtime-release-safety-proposal-v1.0.md
- Backlog issue:
  https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/15
