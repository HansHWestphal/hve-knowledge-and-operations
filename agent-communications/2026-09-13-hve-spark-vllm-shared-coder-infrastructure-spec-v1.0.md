# HVE Spark Shared vLLM Coder Infrastructure Specification

**Date:** 2026-09-13  
**Owner:** Luna, HVE CTO / Head Architect  
**Human approval authority:** Hans Westphal  
**Status:** Historical target specification - not approval to implement or activate

> **Historical record only:** This document describes a proposed target
> architecture as of 2026-09-13. It is not current runtime evidence or
> authorization; revalidate the approved model, host configuration, and
> decision record before any implementation or activation.

## Purpose

This specification defines the shared vLLM infrastructure for HVE coding
agents on the DGX Spark. `hve-coder-jr` and `hve-coder-sr` will use the same
runtime stack and service boundary, but they will not execute concurrently.
The design preserves profile isolation while avoiding two separate coding
model runtimes competing for Spark memory.

This document is a target architecture. It does not authorize installation,
model downloads, service activation, production dispatch, or changes to the
live Hermes-Coder queue.

## Architectural decision

All HVE coding profiles use vLLM as their inference runtime:

| Workload | Runtime | Service model | Execution |
|---|---|---|---|
| `hve-coder-jr` | vLLM | Shared coder endpoint | Exclusive lease |
| `hve-coder-sr` | vLLM | Shared coder endpoint | Exclusive lease |
| `hve-librarian` | Ollama | Existing shared Qwen service | Independent |
| Future `hve-cos` | Ollama | Existing shared Qwen service | Independent |

The coder endpoint is shared infrastructure, not shared agent state. Each
profile retains its own queue, workspace, credentials, tool policy, metrics,
audit trail, lifecycle controls, and rollback lineage.

## Service boundary

The target vLLM service is loopback-only:

```text
Endpoint: http://127.0.0.1:11435/v1
Health:   http://127.0.0.1:11435/health
Models:   http://127.0.0.1:11435/v1/models
```

The endpoint must not be externally bound. Remote access, if later required,
must be introduced through an explicitly approved authenticated gateway rather
than by changing vLLM to listen on all interfaces.

The service must run under a dedicated systemd boundary with:

- a dedicated Unix user;
- an explicit working directory and environment file;
- pinned vLLM, Python, CUDA, and PyTorch provenance;
- a pinned model artifact and checksum;
- loopback binding;
- structured logs;
- restart and stop policy appropriate for a model service;
- an explicit memory and swap contract;
- disabled-first activation until all gates pass.

## Model and configuration contract

The vLLM configuration must pin, record, and expose:

| Field | Requirement |
|---|---|
| Model path or registry identity | Explicit and immutable for each approved profile |
| Model checksum | Required before activation |
| Tokenizer and chat template | Pinned with the model contract |
| Tool parser | Explicitly selected; no implicit auto-detection |
| Context length | Profile-approved and measured on Spark |
| Maximum sequences | One active coder lease initially |
| GPU memory utilization | Measured against Ollama residency and host reserve |
| Swap policy | No swap expansion to conceal memory pressure |
| API port | `127.0.0.1:11435` |
| API authentication | Local boundary only; gateway authentication required if exposed |
| Sampling defaults | Deterministic benchmark profile recorded separately |

The first vLLM proof should use the approved Llama 3.1 8B Instruct artifact
already selected for Jr, unless a separate model decision supersedes it.
`hve-coder-sr` may use a different approved model later, but model selection
must not be inferred from the profile name.

## Exclusive coder lease

Only one coder profile may hold the vLLM lease at a time. The lease manager
must provide:

- acquire with profile identity and job identity;
- explicit lease expiry;
- heartbeat and renewal;
- rejection of a second active holder;
- release on normal completion;
- controlled release on cancellation or timeout;
- recovery evidence when the holder disappears;
- append-only lease events;
- no raw database mutation as an operational bypass.

The vLLM process remains resident while the service is healthy. The lease
controls request authority, not model ownership. A profile without the lease
must not send requests to the endpoint.

If Jr and Sr require different models, model switching is a controlled
maintenance transition: stop new leases, drain or cancel the active job,
capture evidence, load and verify the next pinned model, pass readiness checks,
then grant the next lease. Normal work must not silently trigger model swaps.

## Native tool-call contract

The vLLM OpenAI-compatible endpoint must return structured native tool calls.
The coder supervisor, not the model, remains the authority for tool execution.

Required controls:

- only allowlisted tools may be executed;
- tool names and arguments must pass schema validation;
- paths must remain inside the assigned workspace;
- commands must pass the profile policy;
- commits, pushes, secrets, production services, and broad deletion remain
  denied unless a separate approval gate explicitly permits them;
- textual XML, Markdown, or pseudo-tool markup is never treated as authority;
- malformed, duplicated, or ambiguous calls fail closed with evidence;
- tool results are returned with stable call identifiers;
- multi-tool behavior must be validated explicitly before being enabled.

The vLLM proof must test repeated structured calls across:

```text
read -> tool result -> write -> tool result -> command -> validation
```

A successful `/health` response or one successful tool call is insufficient
for coder readiness.

## Ollama coexistence and Spark capacity

Ollama remains the shared Qwen and embedding runtime on port `11434`, with its
approved hot-residency policy unchanged. vLLM must be measured while the
approved Ollama models are resident.

The capacity test must record:

- total and available memory;
- vLLM RSS and peak RSS;
- GPU memory use and utilization;
- Ollama model residency;
- memory PSI;
- swap use and swap-in;
- request latency and throughput;
- prompt and generated token counts;
- service health and endpoint identity;
- child-process ownership.

No model may be evicted, memory limit raised, context reduced, or swap
boundary weakened merely to make the test pass. If the shared stack cannot
fit safely with approved Ollama residency, dispatch remains blocked until an
approved capacity decision is made.

## Observability

The vLLM service must expose or record:

- model identity and checksum;
- runtime and binary versions;
- request and completion timestamps;
- prompt and output token counts;
- latency;
- HTTP and parser errors;
- active lease holder;
- cancellation and timeout evidence;
- memory and GPU measurements;
- service restart and model-load events.

Preferred inspection commands after implementation:

```bash
systemctl --user status hve-coder-vllm.service --no-pager
curl --fail --silent http://127.0.0.1:11435/health
curl --fail --silent http://127.0.0.1:11435/v1/models
nvidia-smi
free -h
ss -ltn | grep -E ':(11434|11435)\b'
ollama ps
```

These commands are inspection examples only. They do not authorize service
activation or restart.

## Failure and recovery

On a vLLM health, parser, resource, or lease failure:

1. Stop new coder dispatch.
2. Preserve the complete request, response, stderr, service log, and host
   evidence without storing secrets.
3. Revoke the active coder lease.
4. Classify the failure as model, parser, runtime, resource, host, or
   supervisor failure.
5. Clean up only the affected temporary or profile-owned worker state.
6. Leave vLLM inactive if model identity or tool-call readiness is uncertain.
7. Restore the last approved configuration and rerun readiness checks.

A failed vLLM request must never be converted into success, silently retried
under another profile, or routed to Ollama without an explicit policy decision.

## Acceptance gates

Before production activation:

1. Install and pin the approved vLLM environment without changing Ollama.
2. Verify ARM64, CUDA, GB10, PyTorch, and vLLM compatibility.
3. Verify model and tokenizer checksums.
4. Pass health and model-identity checks on loopback.
5. Pass one native structured tool call.
6. Pass repeated multi-turn tool calls through the strict supervisor.
7. Prove path, command, approval, cancellation, timeout, and rollback
   enforcement.
8. Prove Jr and Sr lease exclusion.
9. Measure coexistence with the approved resident Ollama models.
10. Verify service restart, model-load, worker-termination, and recovery
    evidence.
11. Run Jr and Sr profile tests against temporary state only.
12. Publish the evidence and obtain explicit activation approval.

Until every gate passes, vLLM remains a staged runtime and both coder profiles
remain unavailable for production delegation.

## Rollback

Rollback is to the last approved profile-owned runtime configuration. It
includes stopping the staged vLLM service, preserving evidence, releasing the
coder lease, and confirming that Ollama residency and unrelated profiles were
not changed.

Rollback does not include deleting model artifacts, modifying the live Hermes
queue, restarting Ollama, or enabling llama.cpp as an unreviewed fallback.
