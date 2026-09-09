# HVE Hermes Runtime Release Safety Proposal

**Date:** 2026-09-08  
**Version:** 1.0  
**Prepared by:** Luna, HVE CTO / Head Architect  
**Status:** Draft proposal for review  
**Scope:** Shared Hermes runtime deployment and self-update safety  
**Related outage issue:** https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/14

## 1. Purpose

The 2026-09-08 Hermes Chief of Staff outage showed that profile-local
configuration and data boundaries are not enough when multiple gateways execute
from one mutable live Python checkout.

The proposal is not to create a separate Hermes installation for every agent.
The proposal is to keep one shared runtime model while making deployed code
versioned, restorable, and explicitly validated.

## 2. Confirmed incident lesson

The Hermes self-update job fast-forwarded the shared checkout while gateways
were running. The updater then reported that no gateway restart was required.
The resulting mixed in-memory and on-disk Python state caused the Chief of Staff
cron jobs and interactive agent turns to fail on the
`normalize_budget_warning_ratio` import.

The profile boundaries worked for configuration, memory, cron databases,
workspaces, logs, and skills. They did not isolate executable source code or
the Python virtual environment.

## 3. Proposed operating model

### 3.1 Keep practical profile isolation

Continue using one Hermes runtime for the active profiles. Preserve separate
profile-local:

- configuration and environment;
- memory and state databases;
- cron registries and execution history;
- workspaces and logs;
- skills and profile-specific deployment artifacts.

No profile data should be part of a code rollback.

### 3.2 Stop modifying the live checkout in place

The updater should fetch and stage an exact GitHub commit in a versioned
release directory rather than pulling directly into the runtime used by active
gateways.

Suggested layout:

```text
/home/hans/.hermes/releases/<commit-sha>/
/home/hans/.hermes/current -> /home/hans/.hermes/releases/<commit-sha>/
/home/hans/.hermes/profiles/<profile>/
```

### 3.3 Record immutable deployment truth

Each activation should record:

- deployed Git commit SHA;
- Hermes version;
- deployment timestamp;
- previous known-good commit;
- validation results;
- active profile services.

GitHub remains the code source of truth. The local deployment record identifies
what is actually running.

### 3.4 Validate before activation

The staged candidate should pass, at minimum:

- Python import checks;
- targeted Hermes tests available in the checkout;
- `hermes cron doctor`;
- profile service configuration checks;
- a bounded smoke check for each active gateway;
- the x-333 quote validator and other critical local skill checks where
  applicable.

### 3.5 Activate and restart coherently

After validation, the deployment manager should:

1. quiesce or stop dependent gateways;
2. switch the `current` runtime pointer atomically;
3. restart dependent gateway services;
4. verify service health and profile readiness;
5. mark the commit known-good only after verification succeeds.

The update must never report "no restart required" when Python modules or
runtime dependencies changed.

### 3.6 Provide a simple rollback

Rollback should select the previous known-good release, restart dependent
services, and verify health. It must not delete, recreate, or rewind profile
memory, cron history, workspaces, or skills.

## 4. Self-improvement boundary

Hermes self-improvement loops may fetch upstream changes, create branches,
prepare patches, run tests, and produce candidate commits. They must not mutate
the deployed runtime directly.

Promotion into the active release should require an exact GitHub commit and a
successful local deployment gate. Human approval can remain required for
material changes, while routine upstream updates can use the same automated
validation and rollback mechanism.

## 5. Implementation boundary

This proposal is primarily a local deployment-layer change. It should not
require a fundamental fork of the NousResearch Hermes agent codebase.

Likely local components:

- release staging and activation scripts;
- deployment metadata;
- systemd service integration;
- validation and rollback commands;
- replacement of the current in-place self-update behavior.

An upstream Hermes contribution may later be appropriate for generic update
hooks or restart-required signaling, but it is not required for the initial
local implementation.

## 6. Open questions

- Which profiles and services belong in the first activation set?
- Which validation checks are mandatory for every release versus profile
  specific?
- Should upstream updates be auto-promoted after validation or await Hans
  approval?
- How many known-good releases should be retained?
- Should a failed activation automatically roll back or enter an awaiting
  validation state?

## 7. Proposed next step

Create a bounded implementation plan for the local deployment layer. Keep the
first implementation limited to staging, immutable activation, service
restart, deployment recording, validation, and rollback. Do not alter Hermes
agent behavior or profile data contracts in the first phase.
