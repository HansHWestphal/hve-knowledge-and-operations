# HVE Spark Core Inference Operations Runbook

**Date:** 2026-09-13  
**Owner:** Luna, HVE CTO / Head Architect  
**Human approval authority:** Hans Westphal  
**Status:** Approved operating standard; activation remains separately gated

## Purpose

This runbook governs the Spark-local inference services that keep HVE models
hot and ready for bounded work. It covers shared Ollama residency and
profile-owned llama.cpp services. It does not authorize model downloads,
production activation, external binding, vLLM activation, or changes to live
Hermes-Coder queue state.

The authoritative architecture decision is recorded in
`2026-09-13-hve-spark-inference-baseline-v1.0.md`.

## Runtime ownership

| Runtime | Service boundary | Endpoint | Owner |
|---|---|---|---|
| Ollama | Native systemd service | `127.0.0.1:11434` | Shared platform |
| `hve-coder-jr` llama.cpp | Profile-owned user systemd service | `127.0.0.1:11435` | Jr profile |
| Future `hve-coder-sr` | Separate approved service | Separate endpoint | Sr profile |

Every runtime must have a pinned model identity, checksum, binary provenance,
memory envelope, swap policy, health endpoint, logs, metrics, and rollback
reference.

## Desired steady state

The steady state is hot residency:

- Ollama keeps the approved primary, auxiliary, and embedding models resident
  with `OLLAMA_KEEP_ALIVE=24h`.
- Jr keeps its approved llama.cpp model loaded and exposes health and model
  identity on loopback.
- Normal dispatch does not trigger model unload/reload.
- Readiness checks run before dispatch and during service supervision.
- A runtime that fails readiness is removed from dispatch without silently
  routing work through another profile.

Hot residency is a target operating invariant. It must not be achieved by
starting an unapproved service or by exceeding the host memory budget.

## Capacity policy

The Spark has approximately 121 GiB usable memory. The approved baseline
reserves capacity for the three resident Ollama models and a 12 GiB maximum
Jr process envelope. The fourth Ollama model slot is reserved capacity only.

Do not add a resident model, raise a memory limit, lower the swap boundary, or
change context size without a new resource measurement and an approved
configuration change.

## Daily and pre-dispatch inspection

Run the following read-only checks:

```bash
free -h
df -h
nvidia-smi
systemctl is-active ollama
systemctl --user is-active hve-coder-jr-llama.service
ss -ltn | grep -E ':(11434|11435)\b'
ollama ps
```

These checks establish host memory, storage, accelerator visibility, service
state, endpoint residency, and the currently loaded Ollama models.

For Ollama health:

```bash
curl --fail --silent http://127.0.0.1:11434/api/tags >/dev/null
```

For Jr health, when its service has been explicitly activated:

```bash
curl --fail --silent http://127.0.0.1:11435/health
curl --fail --silent http://127.0.0.1:11435/v1/models
```

The reported Jr model ID must match the pinned profile contract. A health
response alone is insufficient if model identity, memory, or tool-call
readiness is wrong.

## Starting and stopping services

Service changes are consequential. Before starting a service:

1. Review the current repository diff and pinned artifact checksum.
2. Confirm the target port is clear or belongs to the expected service.
3. Confirm available memory and current Ollama residency.
4. Confirm the activation approval gate is open.
5. Capture pre-start host and service evidence.

Ollama inspection and restart boundaries:

```bash
sudo systemctl status ollama --no-pager
sudo journalctl -u ollama -n 100 --no-pager
```

Do not restart Ollama as routine maintenance. A restart can evict resident
models and violates the hot-residency objective unless explicitly approved.

Jr inspection boundary:

```bash
systemctl --user status hve-coder-jr-llama.service --no-pager
systemctl --user is-enabled hve-coder-jr-llama.service
```

The Jr unit remains disabled-first until its 12 GiB concurrency evidence and
final activation approval are complete. Do not use `systemctl --user start`,
`enable`, or `restart` as a substitute for approval.

## Monitoring

For active services, monitor:

- model residency and health;
- RSS/HWM and total host available memory;
- memory PSI and swap-in;
- request latency and error rate;
- prompt/generated token metrics;
- llama.cpp child-process ownership;
- Ollama logs and loaded-model state.

Preferred commands:

```bash
ollama ps
htop
free -h
sudo journalctl -u ollama -f
journalctl --user -u hve-coder-jr-llama.service -f
```

If memory pressure, swap activity, repeated health failures, or endpoint
identity drift appears, stop dispatch to the affected runtime and preserve
evidence. Do not unload another profile's model to conceal the condition.

## Model readiness

A model is ready for work only when all of the following are true:

- the service is owned by the expected runtime and profile;
- the expected endpoint is loopback-bound;
- the pinned model identity and checksum are present;
- health and model-list checks pass;
- the configured context and sequence limits match the contract;
- memory and swap limits are enforced;
- native structured tool-call validation passes where tools are required;
- no unresolved stale, cancelled, or ambiguous worker state blocks dispatch.

Text/XML tool markup is not native tool-call readiness and must remain rejected.

## Failure response

On a service or model failure:

1. Stop new dispatch to the affected runtime.
2. Capture service status, logs, endpoint responses, memory, PSI, and model
   residency.
3. Preserve stderr and request metrics.
4. Determine whether the failure is model, runtime, resource, or host related.
5. Stop only the affected service through its known service boundary.
6. Restore the last approved profile-owned configuration if a staged change
   caused the failure.
7. Re-run readiness checks before returning the runtime to dispatch.

Never silently switch model families, bypass checksum validation, grant tool
authority from textual output, or modify another profile's queue or runtime.

## Rollback

Rollback is profile-local and evidence-preserving:

- restore the prior approved configuration;
- restore the prior pinned artifact or symlink;
- leave the affected service inactive if readiness is uncertain;
- retain logs, metrics, and failure evidence;
- verify that Ollama residency and unrelated profiles were not changed.

Rollback does not include broad cleanup, historical queue deletion, model
eviction, or production service restarts without approval.

## Change control

Any change to model, quantization, context, sequence count, memory limit,
binary revision, endpoint, resident Ollama set, or service enablement requires:

1. A versioned configuration change.
2. Targeted tests using temporary state where applicable.
3. Resource and health evidence.
4. Updated GitHub agent communication.
5. Explicit approval for production activation or shared-service changes.

The current baseline is documented and governed, and the 12 GiB Jr concurrency
gate has passed. `hve-coder-jr` remains disabled-first until Hans explicitly
approves production service activation.
