# HVE Spark Qwen3-Coder-Next vLLM Configuration Handoff

**Date:** 2026-09-12  
**Version:** 1.0  
**Status:** Validated installation baseline; runtime launch not yet approved  
**Audience:** Next Hermes-Coder implementation session  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Related systems:** Hermes-Coder, HVE-COS, HVE-Librarian  
**Related plan:** HVE Spark Coding-Session Dual-Mode Configuration v1.0

## Purpose

This communication records the validated local model and vLLM installation
baseline for the next coder session. It does not authorize a runtime profile
transition, service restart, model launch, or change to the normal Hermes
Ollama stack.

## Confirmed local configuration

### Model checkpoint

```text
Model: Qwen/Qwen3-Coder-Next-FP8
Local path: /home/hans/models/3rdparty/Qwen3-Coder-Next-FP8
Format: Sharded Safetensors
Shards: 40/40 present
Index: model.safetensors.index.json present
Approximate checkpoint size: 80.4 GB
```

The shards must not be concatenated, renamed, or converted to GGUF for vLLM.
vLLM should receive the model directory, not an individual shard.

### Isolated serving environment

```text
Environment: /home/hans/.venvs/qwen3-coder-vllm
vLLM: 0.29.0
PyTorch: 2.13.0
Python: 3.12
CUDA packages: CUDA 13 family installed in the environment
```

CUDA visibility and the model index were validated after installation. The
next session must retain the exact command output in its runtime evidence
before launching the model.

## Proposed first launch profile

These settings are a bounded evaluation starting point only. They are not an
approved overnight or production configuration:

```text
Context: 32,768 tokens
Maximum sequences: 1
GPU memory utilization: 0.60
Tool choice: enabled
Tool parser: qwen3_coder
Bind address: 127.0.0.1
Port: 8000
```

Illustrative command:

```bash
/home/hans/.venvs/qwen3-coder-vllm/bin/vllm serve \
  /home/hans/models/3rdparty/Qwen3-Coder-Next-FP8 \
  --served-model-name Qwen3-Coder-Next-FP8 \
  --max-model-len 32768 \
  --max-num-seqs 1 \
  --gpu-memory-utilization 0.60 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --host 127.0.0.1 \
  --port 8000
```

The next coder must not execute this command until the dual-mode preflight is
approved. The preflight must capture Ollama residency, unified memory,
service health, queue state, COS/Librarian status, rollback ownership, and
the effect of releasing the normal 27B model.

## Required validation before runtime use

The next session must validate:

- vLLM starts with the local checkpoint directory;
- the OpenAI-compatible health and model endpoints respond;
- tool-call parsing works with the selected parser;
- streaming and cancellation behave correctly;
- workspace routing remains isolated;
- Hermes-Coder heartbeat and timeout controls remain observable;
- COS and Librarian remain available under the approved auxiliary policy;
- the auxiliary model retains the established 64K minimum context;
- memory remains above the approved floor during a representative bounded run;
- the normal 27B model can be restored without corrupting service state.

Any CUDA, parser, memory, service, or worker ambiguity is a fail-closed
condition. Do not infer successful startup from partial logs or a process that
has not passed endpoint and health validation.

## Operational boundaries

- Do not modify HVE-COS or HVE-Librarian behavior in this handoff.
- Do not change the normal Ollama model policy without explicit approval.
- Do not start an overnight coding session from this document alone.
- Do not use Docker, ad-hoc SQL, broad process termination, or destructive
  cleanup.
- Preserve queue, review, event, workspace, and telemetry evidence.
- The Qwen3-Coder-Next Autobench `0.85 / 32-sequence` profile remains a
  benchmark target, not the default shared Spark profile.
