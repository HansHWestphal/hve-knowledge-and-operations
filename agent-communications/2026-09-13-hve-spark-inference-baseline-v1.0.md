# HVE Spark Inference Baseline

**Date:** 2026-09-13  
**Owner:** Luna, HVE CTO / Head Architect  
**Human approval authority:** Hans Westphal  
**Status:** Approved and technically validated baseline; production activation remains gated

## Decision

HVE adopts a two-tier Spark-local inference baseline:

| Workload | Runtime | Model policy | State ownership |
|---|---|---|---|
| `hve-librarian` | Native Ollama | Existing approved Qwen stack | Shared Ollama service |
| Future `hve-cos` | Native Ollama | Existing approved Qwen stack | Shared Ollama service |
| `hve-coder-jr` | Standalone llama.cpp | Llama 3.1 8B Instruct | Jr-owned runtime and state |
| Future `hve-coder-sr` | vLLM or separately approved runtime | Separate heavyweight model decision | Sr-owned runtime and state |

The profile boundary is deliberate. A profile may consume an approved
inference endpoint, but it must not share another profile's queue, workspace,
credentials, metrics, rollback state, or lifecycle controls.

## Jr target baseline

The target Jr runtime is:

| Field | Target |
|---|---|
| Model | Meta-Llama-3.1-8B-Instruct Q4_K_M |
| Artifact | `/home/hans/models/3rdparty/llama-3.1-8b-instruct/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` |
| SHA256 | `7b064f5842bf9532c91456deda288a1b672397a54fa729aa665952863033557c` |
| Runtime | llama.cpp `0.2.0-dev` |
| llama.cpp revision | `c060ca974c773c7c3d17fd1b66dc9d312bc292c0` |
| Endpoint | `http://127.0.0.1:11435` |
| Context | 65,536 tokens |
| Sequences | 1 |
| Memory envelope | 12 GiB maximum |
| Swap | 0 bytes |
| Tool contract | Native OpenAI-compatible `message.tool_calls` only |
| Activation | Disabled until resource and concurrency evidence passes |

Llama 3.1 passed the native structured tool-call gate but measured
approximately 9.4 GiB RSS/HWM at 64K context with the tested runtime. The
12 GiB envelope is therefore an approved target requiring fresh concurrency
evidence, not a claim that the service is already production-ready.

## Shared Ollama residency

The approved hot-residency set is currently:

1. The primary Qwen model.
2. The auxiliary Qwen model.
3. The embedding model.

`OLLAMA_MAX_LOADED_MODELS=4` is a capacity ceiling, not a requirement to load
four models. The fourth slot remains reserved capacity and must not be assigned
without a separate workload decision and memory evidence.

Ollama remains the native systemd service on loopback port `11434`, with
`OLLAMA_KEEP_ALIVE=24h`. No Ollama model, service, or configuration is changed
by this decision.

## Hot-and-ready invariant

Once the baseline is fully deployed and approved, the intended operating state
is:

- the approved Ollama models remain resident and health-checkable;
- the Jr llama.cpp service remains resident and health-checkable;
- no request depends on serial model unload/reload during normal operation;
- each runtime has an explicit memory, swap, endpoint, model-identity, and
  rollback boundary;
- readiness monitoring detects loss of residency or health before dispatch;
- a failed runtime is isolated rather than silently replaced by another
  profile's runtime.

This invariant does not authorize production activation. Service activation,
Ollama concurrency testing, and final promotion require their own evidence and
explicit Hans approval.

## Acceptance gates

Before Jr is activated for duty:

1. Update the profile-owned llama.cpp contract to the pinned Llama 3.1 artifact
   and 12 GiB envelope.
2. Run the complete Jr test suite and runtime contract checks.
3. Validate native tool calls through the strict provider-neutral validator.
4. Keep the three approved Ollama models resident during bounded Jr workloads.
5. Measure total memory, peak RSS, PSI, swap, latency, Ollama health, and
   endpoint availability.
6. Validate timeout, cancellation, child cleanup, and recovery.
7. Record the evidence in GitHub.
8. Obtain final activation approval before enabling or starting the service.

The model, runtime, tool-call, resource, and three-model Ollama concurrency
gates passed on 2026-09-13. Evidence is recorded in
`2026-09-13-hve-coder-jr-llama-31-baseline-validation-v1.0.md`. Jr remains
inactive until Hans explicitly approves service activation.

## Rollback

Rollback means restoring the prior profile-owned configuration and leaving the
Jr service inactive. It does not mean unloading Ollama models, modifying the
Hermes-Coder live queue, changing another profile, or silently changing the
model or context budget.
