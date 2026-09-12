# HVE Spark Coding-Session Dual-Mode Configuration

**Date:** 2026-09-11  
**Version:** 1.0  
**Status:** Draft for Hans review  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Scope:** DGX Spark model-serving and agent-operation profiles  
**Related systems:** Hermes-Coder, HVE-COS, HVE-Librarian  
**Related benchmark:** [Qwen3-Coder-Next vLLM FP8 DGX Spark Autobench](https://gauravmm.github.io/autobench/configs/qwen3-coder-next-vllm-fp8/)  
**Related operating standard:** `SOPs/2026-09-11-hve-spark-coding-task-sop-v1.2.md`

## 1. Purpose

This document proposes two explicit operating profiles for the DGX Spark:

1. **Coding-session mode** — Hermes-Coder performs a long-running coding
   session, potentially overnight, while HVE-COS and HVE-Librarian remain
   available in a constrained auxiliary mode.
2. **Non-coding-session mode** — Hermes-Coder is idle or not performing a
   long-running coding session, and HVE-COS and HVE-Librarian retain their
   normal operating model and resource priority.

The objective is to make the Spark a reliable shared appliance rather than
allowing one large coding model to consume the entire unified-memory pool.
The profiles must preserve agent availability, human approval, queue
supervision, telemetry, rollback, and safe escalation.

This is a proposed configuration and operating decision for review. It is not
yet an adopted production policy and does not authorize a runtime change,
service restart, model download, deployment, or task-class expansion.

## 2. Decision summary for review

The proposed coding-session arrangement is:

```text
Coding session starts
        |
Unload qwen3.8-hermes:27b-128k from the normal Ollama stack
        |
Keep the 2B auxiliary model and embedding model available
        |
Run Qwen3-Coder-Next-FP8 through a Spark-validated vLLM profile
        |
Keep HVE-COS and HVE-Librarian online using the 2B auxiliary model
        |
Restrict COS and Librarian to lightweight, non-authoritative duties
```

When the coding session ends:

```text
Stop or release the Coder-Next coding profile
        |
Restore qwen3.8-hermes:27b-128k
        |
Return HVE-COS and HVE-Librarian to their normal profile
        |
Verify model, gateway, MCP, queue, and service health
```

The Qwen3-Coder-Next Autobench configuration is the **performance target**,
not the default shared-runtime configuration. Running the target unchanged
beside the existing auxiliary models would leave insufficient memory headroom.

## 3. Evidence and current memory baseline

The current live Spark inspection found:

| Item | Observed state |
|---|---:|
| Unified memory | 121 GiB |
| System memory available during inspection | approximately 63 GiB |
| `qwen3.8-hermes:27b-128k` | 18 GB |
| `qwen3-distill-2b:q4_k_m` | 1.8 GB |
| `nomic-embed-text` | 323 MB |
| Current loaded model total | approximately 20.1 GB |
| HVE-COS gateway | active |
| HVE-Librarian gateway | active |
| Hermes-Coder worker | active |

The model values above are the current `ollama ps` values. They are not a
complete accounting of every process, cache, CUDA allocation, or runtime
reservation. The system must use live monitoring and a controlled preflight
before changing profiles.

## 4. Qwen3-Coder-Next performance target

The target reference is the single-Spark Autobench result for
`Qwen/Qwen3-Coder-Next-FP8` served by vLLM:

| Target attribute | Reference value |
|---|---:|
| Hardware | DGX Spark GB10, ARM64, CUDA 13 |
| Model | `Qwen/Qwen3-Coder-Next-FP8` |
| Runtime | `vllm/vllm-openai:cu130-nightly` |
| Context configured | 65,536 tokens |
| Native model context | 262,144 tokens |
| GPU memory utilization | 0.85 |
| Maximum sequences | 32 |
| Benchmark concurrency | 32 |
| Requests attempted | 1,000 |
| Requests completed within cap | 753 |
| Request errors | 0 |
| Model load plus CUDA graph capture | 428 seconds |
| Prefill throughput | 203.8 tokens/sec |
| Aggregate decode throughput | 184.7 tokens/sec |
| Median time to first token | 618 ms |
| Median time per output token | 167 ms |
| Approximate per-stream decode at concurrency 32 | 5.8 tokens/sec |
| vLLM memory reservation | 105.4 GB |
| FP8 weight footprint reported by benchmark | approximately 40 GB |

The benchmark is valuable evidence that Coder-Next can run on the Spark with
vLLM. It is not Hermes-Coder acceptance evidence: it does not test Hermes
tool calls, repository workspace isolation, queue cancellation, worker
recovery, review quality, or code correctness.

## 5. Shared-memory calculation

If the normal 27B model remains loaded, the approximate model allocation would
be:

```text
Qwen3-Coder-Next vLLM reservation       105.4 GB
qwen3.8-hermes:27b-128k                   18.0 GB
qwen3-distill-2b                         1.8 GB
nomic-embed-text                         0.3 GB
--------------------------------------------------
Approximate combined model allocation  125.5 GB
```

That exceeds the Spark's approximately 121 GiB unified-memory pool before
allowing for the operating system, gateways, MCP servers, queue worker,
CUDA/runtime overhead, filesystem cache, and recovery activity. The full
Autobench profile therefore cannot be treated as a safe shared profile.

If the 27B model is unloaded:

```text
Qwen3-Coder-Next vLLM reservation       105.4 GB
qwen3-distill-2b                         1.8 GB
nomic-embed-text                         0.3 GB
--------------------------------------------------
Approximate combined model allocation  107.5 GB
```

This is materially better, but still leaves only approximately 13–14 GiB
before operating-system and runtime headroom. It is not a comfortable
overnight shared margin at `gpu-memory-utilization=0.85`.

The shared coding profile must therefore use lower vLLM reservation and lower
concurrency than the Autobench target. A starting range for evaluation is:

| Shared profile candidate | Coder reservation | Auxiliary models | Approximate model total |
|---|---:|---:|---:|
| Conservative | 0.60 | 2B + embedding | approximately 76.5 GB |
| Balanced | 0.72 | 2B + embedding | approximately 91.4 GB |
| Autobench target | 0.85 | 2B + embedding | approximately 107.5 GB by reported reservation |

The table scales the reported 105.4 GB reservation directionally and is not a
guarantee of physical usage. vLLM reservation, actual resident pages,
KV-cache growth, CUDA graphs, and Ollama allocations must be measured on the
actual host. The balanced profile must not be adopted merely because its
arithmetic fits; it must demonstrate stable available memory during a
representative long-running task.

## 6. Proposed profile definitions

### 6.1 Non-coding-session profile

**Purpose:** Normal HVE operations when Hermes-Coder is idle or not conducting
a long coding session.

**Model allocation:**

- `qwen3.8-hermes:27b-128k` remains available.
- `qwen3-distill-2b:q4_k_m` remains available for auxiliary work.
- `nomic-embed-text` remains available.
- HVE-COS and HVE-Librarian use their normal routing and model policy.

**Behavior:**

- Normal COS and Librarian task quality is preserved.
- Hermes-Coder may remain ready, but must not start an unbounded coding
  session without an explicit profile transition.
- No Coder-Next vLLM reservation is kept active solely for convenience.
- The system verifies that all normal gateways, MCP services, and the queue
  worker are healthy.

### 6.2 Coding-session profile

**Purpose:** Long-running Hermes-Coder implementation work, including
overnight sessions, while keeping COS and Librarian available.

**Model allocation:**

- Unload or stop serving `qwen3.8-hermes:27b-128k` from the normal Ollama
  stack.
- Keep `qwen3-distill-2b:q4_k_m` available.
- Keep `nomic-embed-text` available if required by COS, Librarian, or
  repository knowledge workflows.
- Start Qwen3-Coder-Next FP8 through the validated vLLM compatibility path.

**Initial serving settings for evaluation:**

```text
Model: Qwen3-Coder-Next-FP8
Context: 32K initially; 64K only after stability evidence
GPU memory utilization: begin at 0.60–0.72
Maximum sequences: 1–2
Prefix caching: enabled
Attention backend: FlashInfer if validated on the selected build
Tensor parallelism: 1
Tool parser: qwen3_xml pending Hermes-specific validation
```

The Autobench `0.85 / 32-sequence / 65K` configuration remains a benchmark
lane. It should not be the default overnight shared setting.

**Agent behavior:**

- Hermes-Coder receives the primary coding workload.
- HVE-COS and HVE-Librarian remain online through the 2B auxiliary model.
- COS and Librarian are restricted to lightweight, non-authoritative work:
  monitoring, routing, status communication, retrieval, simple extraction,
  classification, queue supervision, and escalation.
- Major architecture, policy, financial, security, approval, or destructive
  decisions are deferred, escalated, or held for the 27B model or human
  review.
- Missing confidence or degraded model capability must produce an explicit
  escalation, not a success-shaped answer.

**Context requirement:**

The auxiliary Hermes model must retain the established minimum 64K context
requirement. The coding profile must not silently reduce the auxiliary agent
below that minimum to make room for Coder-Next. If the combined context and
KV-cache requirements cannot fit safely, the profile must fail closed and
escalate rather than silently degrading context.

## 7. Profile transition controls

A profile transition is a controlled runtime operation, not a model preference
toggle.

### 7.1 Entering coding-session mode

Before starting Coder-Next, the supervisor must:

1. Confirm no critical COS, Librarian, CFO, UAT, or deployment activity is
   using the normal 27B model.
2. Record the coding-session ID, operator, purpose, expected duration, and
   rollback owner.
3. Capture a baseline of `free -h`, GPU/runtime memory, loaded models,
   gateway health, queue state, and active services.
4. Confirm that no protected live task or approval-gated workflow would be
   disrupted.
5. Stop or unload the 27B model through its supported service interface.
6. Verify that the 27B allocation has actually been released.
7. Start the Coder-Next vLLM service with the bounded shared profile.
8. Verify the OpenAI-compatible endpoint, tool-call parser, metrics endpoint,
   and model identity.
9. Run a non-mutating workspace-routing and tool-call smoke test.
10. Confirm safe memory headroom before dispatching coding work.

If any step fails, the transition stops and the normal profile is restored.

### 7.2 Returning to non-coding-session mode

The supervisor must:

1. Stop new coding dispatch.
2. Allow the current bounded task to reach a safe terminal state or cancel it
   through the supported queue API with an explicit reason.
3. Capture final queue, worker, workspace, telemetry, and vLLM evidence.
4. Stop or release the Coder-Next service.
5. Verify its memory allocation is released.
6. Restore `qwen3.8-hermes:27b-128k`.
7. Restore normal COS and Librarian routing.
8. Verify the 2B auxiliary model, embedding model, gateways, MCP services,
   queue worker, and relevant services.
9. Record the transition result and any recovery action.

No profile transition may use ad-hoc SQL, destructive cleanup, broad process
termination, or inference about an ambiguous worker state.

## 8. Monitoring and safety requirements

During coding-session mode, supervision must monitor:

- unified memory available and used;
- vLLM KV-cache utilization;
- vLLM prefill and decode throughput;
- time to first token and inter-token latency;
- Hermes-Coder heartbeat and progress;
- queue status and claimed/executing jobs;
- COS and Librarian gateway health;
- 2B auxiliary model availability;
- embedding service availability;
- CUDA/runtime errors;
- OOM or allocation-failure messages;
- worker child processes and cancellation behavior.

The coding session must stop or degrade safely if:

- available memory falls below the approved floor;
- vLLM reports repeated preemption or allocation failures;
- COS or Librarian becomes unavailable;
- the worker misses its heartbeat or no-progress deadline;
- tool-call parsing becomes unreliable;
- workspace routing diverges;
- telemetry becomes incomplete;
- the session exceeds its approved time or scope budget.

The system must not silently kill COS, Librarian, the queue worker, or the
vLLM server to recover memory. Recovery must identify the owning process and
use the supported service or queue operation.

## 9. Validation plan before adoption

The dual-mode configuration should not become an operating default until the
following evidence exists on the actual Spark:

### Runtime validation

- Coder-Next FP8 loads reliably using a pinned, Spark-compatible vLLM build.
- The model remains stable at 32K context with the 2B and embedding models
  loaded.
- 64K context is tested separately before being considered available.
- The memory floor remains healthy during a long run.
- The 27B model can be unloaded and restored without corrupting normal service
  state.

### Hermes-Coder validation

- OpenAI-compatible endpoint integration works.
- `qwen3_xml` or the selected parser handles long tool calls correctly.
- Tool calls, streaming, cancellation, and timeout behavior work.
- Workspace isolation remains correct.
- Usage, tokens, turns, tool calls, timing, and model identity are captured.
- Review, safety, and recovery gates remain unchanged.

### COS and Librarian validation

- Both gateways remain reachable while Coder-Next runs.
- Both can complete lightweight monitoring, routing, retrieval, and
  communication tasks using the 2B model.
- Their 64K minimum context requirement is preserved.
- Low-confidence or unsupported work escalates explicitly.
- No major decision is made solely by the degraded 2B mode.

### Shared-session pilot

Run a bounded pilot with:

- one Hermes-Coder job at a time;
- one or two maximum Coder-Next sequences;
- fresh isolated workspaces;
- a fixed cohort deadline;
- minute-level progress reporting;
- a no-progress watchdog;
- supported cancellation;
- final memory and service snapshots;
- separate evidence for coding, COS, and Librarian behavior.

The existing Phase 6 pilot thresholds remain applicable to the coding task:
100% safety pass, at least 90% review pass, no more than 20% intervention,
and no more than 10% recovery. Shared-mode availability of COS and Librarian
must be an additional acceptance criterion.

## 10. Rollback

Rollback from coding-session mode must be possible without deleting historical
queue, review, event, workspace, or telemetry evidence.

The known-good rollback sequence is:

```text
Stop new coding dispatch
        |
Safely complete or cancel the bounded coding job
        |
Capture evidence
        |
Release Coder-Next
        |
Restore qwen3.8-hermes:27b-128k
        |
Restore normal COS/Librarian routing
        |
Verify health and memory
```

If Coder-Next fails to start, the session remains in the non-coding profile.
If Coder-Next fails during execution, Hermes-Coder enters the existing
controlled failure and recovery path. The system must not infer success from a
partial output or ambiguous worker termination.

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Coder-Next consumes the shared memory pool | Unload 27B; use low sequence count and bounded vLLM reservation |
| 2B COS/Librarian quality is insufficient | Restrict duties, preserve 64K context, escalate low-confidence work |
| vLLM reservation differs from physical usage | Measure resident memory and available memory during a long pilot |
| Tool calls fail on long inputs | Validate parser behavior; start with `qwen3_xml` |
| 428-second cold start delays recovery | Pre-stage weights and treat startup as an explicit availability budget |
| Coding worker starves other agents | Monitor memory and agent health; enforce fail-closed floors |
| Profile transition disrupts a live task | Require preflight, protected-task checks, and supported cancellation |
| Floating runtime changes behavior | Pin the vLLM image/build and record its digest or commit |
| 64K context causes KV-cache pressure | Begin at 32K and validate 64K separately |
| Overnight job runs without supervision | Keep cohort deadline, heartbeat, no-progress watchdog, and minute reporting |

## 12. Items requiring Hans review

1. Approve the dual-mode operating concept.
2. Confirm that COS and Librarian may use the 2B auxiliary model during a
   coding session.
3. Confirm that major COS/Librarian decisions must be deferred or escalated
   during degraded mode.
4. Approve the initial shared-profile memory range of 0.60–0.72 for testing.
5. Approve preserving the Autobench `0.85 / 32-sequence` configuration as a
   benchmark target rather than an overnight production default.
6. Approve a controlled shared-mode pilot before any profile automation or
   production default change.
7. Confirm the desired memory floor and maximum overnight coding-session
   duration.

## 13. Current status

**Draft for Hans review.**

No runtime profile has been changed by this document. The current normal model
stack, Hermes services, queue, and worker remain unchanged. The next
implementation step, if approved, is to design and validate the profile
transition and shared-mode pilot without changing normal operating defaults.
