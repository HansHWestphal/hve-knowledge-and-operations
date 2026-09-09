# HVE Agent Communication: Mercury Phase 8 Live-Validation Briefing

**Date:** 2026-09-03  
**Owner:** Luna, HVE Head Architect and CTO  
**Authority:** Hans Westphal, HVE CEO  
**Status:** Validation stopped; AI-only rollback complete; resume deferred  
**Repository:** [`humanvalueexchange/mercury-node`](https://github.com/humanvalueexchange/mercury-node)  
**Validated commit:** [`fcaacda`](https://github.com/humanvalueexchange/mercury-node/commit/fcaacdadadca6984262ae0c2d90686518de9d7ea)  
**Related plan:** [`2026-09-03-hve-mercury-split-implementation-plan-v1.0.md`](https://github.com/HansHWestphal/hve-knowledge-and-operations/blob/hermes/local-llm-evaluation-harness/agent-communications/2026-09-03-hve-mercury-split-implementation-plan-v1.0.md)

## Purpose

This briefing records exactly what was accomplished during the authorized
Phase 8 Mercury Hailo + CPU split-reasoning validation window, the evidence
obtained, the blockers encountered, the final live state, and the conditions
required before work resumes.

This is an operational handoff and evidence summary. It is not a promotion
decision. The reviewed split architecture was not promoted.

## Executive outcome

The readiness-access implementation was corrected, frozen, pushed, deployed,
and verified successfully. The actual Hailo runtime also demonstrated stable
warm direct requests after its cold-load period.

End-to-end Phase 8 promotion nevertheless remains blocked because the
Hailo-only fallback did not return a valid Hailo plan within the approved
2.5-second planner budget. When the CPU endpoint was intentionally made
unavailable, `mercury ask` returned the unavailable response instead of the
required Hailo `answer_sketch`.

A second independent blocker was observed in normal Hailo service logging:
the runtime logged the full planner prompt and live snapshot. No seeds,
macaroons, passwords, private keys, backup tokens, or RPC credentials were
observed, but unrestricted prompt/snapshot logging does not satisfy the
Phase 8 secrecy requirement.

The validation was stopped at that point. The reviewed AI artifacts were
rolled back, the temporary `mercury-ready` group was removed, and all
protected services remained operational.

## Authorized scope and boundaries

Hans authorized a controlled live validation using only the reviewed Mercury
artifacts from the Hailo + CPU split branch. The approved boundaries remained:

- Hailo planner on `127.0.0.1:8000`;
- native llama-server on `127.0.0.1:8089`;
- Mercury Agent on `127.0.0.1:8088`;
- approved Qwen Hailo and CPU models;
- CPU service user `mercury-llm`;
- CPU affinity cores 2-3;
- two CPU threads;
- CPU context size 8192;
- reasoning disabled;
- no remote DGX fallback;
- no Docker, vLLM, stock Ollama, alternate models, or retired Hailo-8L path;
- no `/api/tools/{name}/execute` calls;
- no payment, invoice, channel, fee, Magma, wallet, or confirmation-gate
  operation.

Bitcoin Core and LND remained the authoritative money layer and were not
modified.

## Repository implementation completed

The following readiness-access implementation was completed in the Mercury
repository:

1. `HailoClient.ready()` now handles only the expected observation failures:
   `PermissionError`, `FileNotFoundError`, and `NotADirectoryError`. These
   conditions return `False` and allow approved degraded behavior instead of
   terminating the CLI.
2. A higher-level CLI test verifies that a false Hailo readiness result causes
   no Hailo POST and continues through the CPU draft path.
3. A dedicated `mercury-ready` access contract was added for the readiness
   directory and marker.
4. The prewarm marker is published with group-readable mode `0640`.
5. Hailo runtime-directory lifecycle handling uses `RuntimeDirectoryPreserve=no`.
6. The operator access contract was documented without granting `hermes`
   membership in `hailo-ollama`.
7. Offline tests and Python compilation were run successfully.

The implementation was frozen and pushed through these commits:

- `f835b5a` — defensive readiness handling, marker permissions, group
  contract, documentation, and tests;
- `511c545` — attempted privileged runtime-directory ownership preparation;
- `fcaacda` — empirical correction using `mercury-ready` as the Hailo and
  prewarm primary group, with `hailo-ollama` retained as supplementary access
  for Hailo data.

The final validated commit was `fcaacda`. The Mercury worktree was clean after
the commit and push.

## Live validation chronology

### First authorized run

The first deployment used the frozen reviewed commit `173e857`. A narrow
rollback copy was created before installation. Hailo prewarm completed and
created readiness, but the first warm request returned HTTP 500.

Subsequent review identified that the shell diagnostic had constructed
malformed JSON. The Hailo server returned an oatpp JSON parser error:

```text
Unknown character
```

After correcting the request encoding, valid delayed requests returned HTTP
200 in approximately 427 ms and 418 ms. Hailo remained at a stable PID with
no service restart. This corrected the initial diagnosis: the first observed
500 was a probe-construction error, not proof of persistent Hailo runtime
failure.

### Second run and readiness integration blocker

The readiness fix was deployed and the Hailo prewarm completed. Five direct
warm Hailo requests returned HTTP 200 in approximately 413-417 ms, with a
stable PID and no restart.

The Mercury CLI then failed before reaching the engine orchestration because
the operator could not inspect the readiness marker:

```text
PermissionError: [Errno 13] Permission denied: '/run/hailo-ollama/ready'
```

The marker directory was owned by `hailo-ollama:hailo-ollama` with mode `0750`,
and the marker was mode `0600`. The `hermes` operator was not a member of
`hailo-ollama`.

This led to the defensive `ready()` fix and the dedicated group-access
implementation.

### Third run and systemd ownership correction

The first version of the group contract used `SupplementaryGroups` plus
privileged `chgrp`/`chmod` commands. On the live host, systemd still left the
runtime directory owned by `hailo-ollama:hailo-ollama`, so `hermes` could not
traverse it.

The deployment was rolled back. The unit was corrected empirically to use:

- Hailo primary group: `mercury-ready`;
- Hailo supplementary group: `hailo-ollama`;
- prewarm primary group: `mercury-ready`;
- prewarm supplementary group: `hailo-ollama`.

This preserved access to `/var/lib/hailo-ollama` while making the systemd
runtime directory group-compatible with the operator.

The corrected deployment produced:

```text
/run/hailo-ollama       hailo-ollama:mercury-ready 0750
/run/hailo-ollama/ready hailo-ollama:mercury-ready 0640
```

The `hermes` operator could read the marker successfully. Hailo restart
removed the marker, manual prewarm recreated it, and all protected services
remained active.

## Third-run validation results

### Passed

- Exact frozen commit deployment.
- Dedicated group membership restricted to `hermes` and `hailo-ollama`.
- Operator access to the readiness marker.
- Readiness absent after Hailo restart.
- Manual prewarm completion.
- Hailo and CPU localhost bindings.
- Approved CPU model and llama-server settings.
- Bitcoin Core, LND, and Mercury Agent operational state.
- Zero-channel deterministic response.
- Node sync/readiness deterministic response.
- Hailo unavailable -> CPU draft fallback.
- Both engines unavailable -> unavailable response with nonzero exit.
- No state-changing tool or money-layer operation.

### Not applicable

The active-channel liquidity-percentage fast path was not applicable because
the live snapshot had zero active channels. The question correctly did not use
that fast path.

### Failed promotion gates

#### Hailo-only fallback

With the CPU endpoint intentionally pointed at an unused localhost port and
Hailo marked ready, the CLI returned:

```text
Mercury AI unavailable (local engines down).
```

with exit code `1`, rather than returning a valid Hailo plan sketch.

Debug timing reported approximately:

```text
parallel=2504ms
```

The Hailo journal showed the planner prompt beginning, but no completed valid
planner response within the approved 2.5-second Hailo stage budget. This
fails the required CPU-unavailable -> Hailo-sketch fallback behavior.

#### Planner-shaped Hailo latency

The trivial direct Hailo probe was fast after warm-up, but the actual
planner-shaped request containing the Mercury system prompt and snapshot did
not complete within the approved Hailo planner budget. This means the
trivial warm-probe result cannot be used as evidence that the split planner
stage meets contract.

#### Prompt and snapshot logging

The Hailo runtime journal printed the full planner system prompt and the live
snapshot. The captured snapshot included operational node and wallet fields,
but the actual values are intentionally not reproduced in this repository
briefing.

No high-sensitivity credential material was observed. Nevertheless, full
prompt and snapshot logging violates the required normal-log redaction
boundary and remains a promotion blocker until corrected or explicitly
re-scoped through review.

### Not completed

The following were not run because the Hailo-only gate failed:

- ten-identical-ask warm soak;
- warm Mercury ask p50 and p95;
- merge-success validation;
- merge-failure and merge-budget fallback validation;
- full malformed-plan end-to-end validation;
- zram soak comparison;
- thermal and throttle soak comparison;
- complete CLI-level secrecy review;
- final confirmation-gate regression validation.

No promotion claim is made.

## Rollback and current live state

Rollback copy for the final attempt:

`/var/backups/mercury-ai-phase8-20260903-213840`

The final rollback:

- restored the prior Mercury CLI and package;
- removed the reviewed AI package and prewarm artifacts;
- removed the temporary `mercury-ready` group;
- removed the readiness marker;
- ran `systemctl daemon-reload`;
- restarted only `hailo-ollama.service`.

Current verified state:

- Hailo service active;
- CPU LLM service active;
- Bitcoin Core active;
- LND active;
- Mercury Agent active;
- Hailo, CPU, and Agent listeners remain localhost-only;
- prewarm timer absent/disabled;
- no reviewed split artifacts remain installed;
- no `mercury-ready` group remains;
- wallet, payment, channel, fee, Magma, and confirmation state untouched.

## Decisions for tomorrow

The next work session should not begin with another live soak. First obtain
review and approval for the following narrow technical decisions:

1. How to make the actual Hailo planner request meet the fixed 2.5-second
   stage budget without changing the approved model or architecture.
2. Whether prompt compaction, output ceiling, or another evidence-based
   optimization is sufficient, based on measured planner timing.
3. How to prevent normal Hailo runtime logs from printing full prompts and
   snapshots, or whether a scoped runtime logging contract must be addressed
   outside the Mercury repository.
4. Whether Hailo-only fallback may remain blocked until planner completion is
   reliable, or whether the architecture requires a reviewed behavior change.
5. Whether the readiness marker should continue to mean “prewarm completed”
   while planner stability remains a separate gate.

No timer enablement, model change, timeout increase, remote fallback, service
identity expansion, or money-layer change is authorized by this briefing.

## Resume criteria

Before another live run:

- a reviewed commit must address the Hailo-only fallback failure or document
  an approved alternative;
- Hailo normal-log prompt/snapshot exposure must be corrected or explicitly
  dispositioned;
- offline tests must cover the final fallback behavior;
- the live host must start from the rolled-back state;
- any required host group or identity change must be explicitly authorized;
- the exact frozen commit and artifact hashes must be recorded;
- manual readiness, planner-shaped Hailo timing, and operator-access gates must
  pass before deterministic tests;
- the ten-ask soak remains the final gate.

## Evidence boundary

This briefing records operational outcomes without committing credentials,
raw snapshots, wallet values, private databases, unrestricted logs, or runtime
state. The live host remains the source of truth for detailed evidence, while
this document records the bounded decisions, results, and blockers needed for
agent coordination.
