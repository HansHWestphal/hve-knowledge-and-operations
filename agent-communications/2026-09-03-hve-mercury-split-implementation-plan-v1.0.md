# HVE Mercury Split Architecture Implementation Plan

**Date:** 2026-09-03  
**Author:** Luna, HVE Head Architect and CTO  
**Status:** Proposed for Hans review  
**Scope:** `humanvalueexchange/mercury-node` repository implementation  
**Related architecture:** `MN-ARCH-REASON-001`  

## Purpose

This document proposes the implementation plan for the next Mercury CLI
architecture revision. It incorporates the live failure analysis and the two
approved behavioral decisions below. It is a review artifact, not authorization
to change the live `mercury` host.

The Mercury design remains a standalone Bitcoin, Lightning, and local-AI
appliance. Bitcoin Core and LND remain the authoritative money layer. The AI
layer remains advisory and must not execute tools, pay invoices, move funds,
open or close channels, set routing fees, buy Magma, or bypass existing human
confirmation gates.

## Decisions incorporated

### Decision 1 — Optional CPU merge under deadline pressure

CPU llama-server merge remains in the code path and remains the quality path.
It is optional when the global request deadline cannot safely accommodate it.

Allowed behavior:

- Run merge only when both the Hailo plan and CPU draft are valid.
- Run merge only when at least three seconds remain within the 12-second global
  ask budget.
- Otherwise return the CPU draft when available.
- If no CPU draft exists, return the Hailo `answer_sketch` plus no more than
  three bullets.
- Keep the operator-facing label as `Local`.
- Expose merge state only through debug stderr output:
  `merge=ran`, `merge=skipped_budget`, or `merge=skipped_partial`.

This does not authorize removing merge, adding another model, using Hailo as a
merger, or raising the draft, merge, or total timeout contracts.

### Decision 2 — Closed deterministic snapshot responses

Deterministic responses are authorized only for the following v1 cases:

| Case | Required condition | Permitted result |
|---|---|---|
| Zero channels / channel status | `totals.active == 0` | Snapshot-derived no-channel status |
| Sync / node readiness | Chain and wallet fields are present | Height, sync state, and wallet totals |
| Liquidity one-liner | At least one active channel and the question asks only for inbound/outbound percentages | Snapshot-derived totals and percentages |

The fast path must:

- match a closed intent list;
- use only the already-built snapshot;
- perform no additional HTTP, `lncli`, Hailo, llama-server, or tool calls;
- reject stale or incomplete required fields;
- remain advisory;
- never recommend a peer, amount, invoice, payment, fee, or channel action;
- fall through to DualEngine for every other question.

A general English rule engine, a second snapshot harvest, and any
`/api/tools/{name}/execute` call are not authorized.

## Implementation principles

1. Measure the deployed runtime before changing repository behavior.
2. Preserve the approved engines, ports, models, and CPU service contract.
3. Make cold Hailo loading a service-readiness concern, not a user-request
   timeout concern.
4. Preserve valid partial results instead of requiring both engines to succeed.
5. Keep all snapshot and model-output handling bounded, validated, and
   secret-free.
6. Do not make live unit, package, model, boot, PCIe, or money-layer changes as
   part of repository implementation.

## Phase 0 — Required live measurements before coding

The existing live services may be observed and queried locally for measurement.
No live systemd unit or runtime configuration changes are included in this
phase.

### Hailo residency measurements

Capture a clean, isolated sequence:

1. Send one minimal, non-sensitive Hailo request with a long diagnostic client
   timeout so model loading is not cancelled.
2. Record model replacement and completed-response duration.
3. Run five sequential short requests and record each latency.
4. Leave the service idle, then issue a short request and record whether model
   replacement recurs.
5. Test request-level `keep_alive: -1` separately from the environment setting.
6. Test two overlapping requests and determine whether the second waits, fails,
   or triggers another model replacement.

The measurements must distinguish:

- HTTP server readiness;
- model registration;
- HEF/model configuration;
- completed warm inference;
- cancellation and reload behavior.

### CPU measurements

Capture the actual draft request behavior without changing the approved service
unit:

- prompt token count;
- prompt-processing duration;
- decode duration and token rate;
- generated token count;
- repeated identical-prefix behavior;
- prefix-cache hit/miss evidence where exposed by the deployed build.

Measure both the current prompt and a compact candidate prompt. Do not assume
that shortening the answer removes the prompt-prefill cost.

### Measurement decision gate

The measurements will determine whether the Hailo fix is primarily:

- model prewarming;
- model-store/configuration correction;
- request serialization;
- runtime retention behavior;
- source-build/runtime incompatibility;
- or another issue requiring separate review.

They will also determine whether CPU prompt compaction and cache reuse can meet
the fixed two-thread/cores-2–3 contract. No implementation claim will be based
on assumed token rates.

## Phase 1 — Deterministic status fast paths

Add an isolated, unit-testable fast-path module. It will receive the already
validated snapshot and a closed question intent, then render fixed sentence
templates.

It will not perform network access or invoke any backend. It will reject
missing, stale, or type-invalid fields and return control to DualEngine.

Candidate implementation surface:

```text
src/cli/mercury_cli/ai/fast_path.py
src/cli/mercury
tests/test_fast_path.py
tests/test_dual_engine.py
```

Tests will cover:

- each authorized case;
- missing fields;
- stale snapshots;
- zero-channel behavior;
- out-of-scope questions;
- refusal to include peer, payment, fee, or invoice recommendations;
- no additional client calls.

## Phase 2 — Deadline-driven DualEngine orchestration

Replace the current gather-then-decide behavior with completion-driven result
handling and one global 12-second deadline.

Target flow:

```text
Build one snapshot
  -> authorized fast path: return Local response
  -> otherwise start Hailo plan and CPU draft concurrently
  -> retain each valid completed result
  -> merge only when both are valid and >=3 seconds remain
  -> otherwise return draft or plan sketch
  -> return unavailable only when no valid result exists
```

Required behavior:

- Hailo failure does not discard a valid CPU draft.
- CPU failure does not discard a valid Hailo plan.
- Merge failure returns the valid draft.
- A merge skipped for budget returns the valid draft or plan sketch.
- Unfinished requests are explicitly cancelled and cleaned up.
- Both-engine failure returns a clear unavailable result and nonzero exit.

Debug stderr output will include separate fields for:

```text
snapshot_ms
hailo_ms
draft_ms
merge_ms
total_ms
source
hailo_ready
merge=ran|skipped_budget|skipped_partial
```

Default stdout will not disclose backend names, model names, stage names, raw
plan JSON, or orchestration details.

Candidate implementation surface:

```text
src/cli/mercury_cli/ai/engine.py
src/cli/mercury_cli/ai/render.py
tests/test_dual_engine.py
```

## Phase 3 — Hailo readiness and prewarming

This phase depends on Phase 0 evidence.

If completed prewarming produces stable warm inference, add a reproducible
readiness contract:

- send request-level `keep_alive: -1` in addition to the service environment;
- use a minimal non-sensitive prewarm prompt;
- mark readiness only after completed inference;
- invalidate readiness on service restart;
- serialize Hailo requests so a second request cannot trigger concurrent graph
  replacement;
- make the CLI skip Hailo when it is not ready rather than using a user request
  to initiate cold loading.

A readiness marker, if used, should be systemd lifecycle-managed under `/run`,
not persistent storage. It must not survive a Hailo service restart as a false
claim.

Possible repository surface:

```text
src/cli/mercury_cli/ai/hailo_client.py
scripts/systemd/hailo-ollama.service
scripts/systemd/mercury-hailo-prewarm.service
scripts/systemd/mercury-hailo-prewarm.timer
```

The prewarm mechanism must not include wallet, channel, node, or operator
question data.

If the source-built runtime still reloads or replaces the model after a
completed prewarm, that remains a promotion blocker and must not be concealed
by increasing the user planner timeout.

## Phase 4 — CPU prompt and merge optimization

Based on measured token and timing data:

- compact the AI-facing snapshot while preserving the 4 KB source snapshot
  cap;
- stabilize the draft system prompt byte-for-byte;
- remove redundant prompt instructions;
- select a measured output ceiling rather than assuming 48 or 96 tokens;
- use a stop sequence only if verified by the deployed llama-server;
- compact the merge input and output;
- skip merge when the global deadline cannot accommodate it.

The following must remain unchanged:

- Qwen3.8-2B-Distill-Q4_K_M GGUF;
- native llama-server;
- `--threads 2`;
- CPU affinity cores 2–3;
- `--ctx-size 8192`;
- `--reasoning off`;
- localhost-only binding;
- dedicated non-root service account.

Candidate implementation surface:

```text
src/cli/mercury_cli/prompts.py
src/cli/mercury_cli/ai/engine.py
src/cli/mercury_cli/ai/llama_client.py
tests/test_dual_engine.py
```

## Phase 5 — Hailo schema and logging hardening

Hailo plan parsing will:

- normalize only an explicitly closed alias map;
- validate intent and action enums;
- validate all field types;
- bound string and list lengths;
- restrict tool-intent vocabulary;
- drop unknown keys;
- reject malformed or contradictory data;
- never convert plan content into executable actions.

Normal service and CLI logs should contain metadata and timings, not full
snapshots, prompts, or model responses. The `hailort.log` warning will be
investigated and corrected only through a scoped repository service-contract
change if it is shown to affect configuration or reliability.

## Phase 6 — Offline validation and documentation

Add or update offline tests for:

- all three deterministic cases;
- stale and incomplete snapshots;
- Hailo readiness absent/present;
- known Hailo aliases;
- malformed Hailo JSON;
- partial engine success;
- merge skipped by budget;
- merge failure fallback;
- explicit cancellation cleanup;
- all engines unavailable;
- secret-free prompt construction;
- default output redaction.

Update Mercury documentation with:

- the optional-merge decision and limits;
- the closed deterministic fast-path decision and limits;
- measured Hailo and CPU runtime facts;
- remaining promotion blockers;
- the unchanged Mercury/HVE-LIFE-OS/HVE-CFO and money-layer boundaries.

The HVE approval record and this plan remain distinct from Mercury runtime
documentation. No draft, transient runtime state, credentials, or unapproved
policy will be committed.

## Phase 7 — Repository validation

Before any live deployment proposal:

- run the existing offline test suite;
- run Python compilation;
- run diff and whitespace checks;
- validate systemd syntax where supported;
- verify localhost-only endpoint configuration;
- inspect for generated caches and unrelated changes;
- verify no engine, model, port, thread, context, or confirmation-gate drift.

## Phase 8 — Separate live validation proposal

After code review, live changes require separate explicit authorization. The
proposed validation sequence is:

1. Install reviewed repository artifacts only.
2. Start or verify Hailo prewarm and readiness.
3. Test the three deterministic cases.
4. Test Hailo-only, CPU-only, and dual-engine fallback paths.
5. Run ten identical warm asks.
6. Measure warm p50 and p95.
7. Measure zram growth, thermal state, and throttle bits.
8. Check prompt/log/output secrecy.
9. Verify payment, channel, and confirmation-gate behavior remains unchanged.

## Promotion blockers

Promotion must stop if any of these occur:

- Hailo warm planner requests do not meet the 2.5-second target.
- Hailo model replacement recurs during warm sequential requests.
- Hailo readiness is stale, false, or not invalidated after restart.
- CPU draft cannot meet its approved stage budget after evidence-based
  optimization.
- Full-path behavior exceeds the 12-second total budget.
- Merge failure or budget skipping discards a valid draft.
- Deterministic fast paths use stale/incomplete data or intercept open-ended
  questions.
- Any secret appears in prompts, logs, or operator output.
- Any Bitcoin Core, LND, wallet, payment, channel, fee, Magma, or confirmation
  gate behavior changes.
- zram, thermal, or throttle validation fails.

## Review request

Please review and approve or amend this implementation plan before Phase 1
repository coding begins. The immediate next action after approval is the
read-only measurement phase, followed by the narrow deterministic fast-path
implementation. This document does not authorize live unit changes or
production promotion.
