# HVE Spark llama.cpp Runtime Runbook

**Status:** Implemented, disabled pending activation approval  
**Owner:** Luna, HVE CTO / Head Architect  
**Human approval authority:** Hans Westphal  
**Scope:** `hve-coder-jr` standalone llama.cpp runtime only

## Purpose

This runbook defines the governed Spark-local llama.cpp runtime boundary used
by `hve-coder-jr`. It does not replace or modify the shared Ollama service and
does not activate or configure vLLM.

The runtime is profile-owned at the process, endpoint, model identity, logs,
health evidence, and resource-budget layers. The llama.cpp binary is currently
the validated ARM64 build from the HVE Life OS tree and remains subject to
source and build provenance review before future upgrades.

## Approved baseline

| Item | Value |
|---|---|
| Profile | `hve-coder-jr` |
| Runtime | llama.cpp `0.2.0-dev` |
| llama.cpp revision | `c060ca974c773c7c3d17fd1b66dc9d312bc292c0` |
| Binary | `/home/hans/hve-life-os/src/build/bin/llama-server` |
| Model | Qwen2.5-Coder-7B-Instruct Q4_K_M |
| Model file | `/home/hans/models/3rdparty/qwen2.5-coder/qwen2.5-coder-7b-instruct-q4_k_m.gguf` |
| Model SHA256 | `509287f78cb4d4cf6b3843734733b914b2c158e43e22a7f4bf5e963800894d3c` |
| Endpoint | `http://127.0.0.1:11435` |
| API model ID | `qwen2.5-coder-7b-instruct-q4_k_m` |
| Context target | 65,536 tokens |
| Sequences | 1 |
| Memory budget | 8 GiB |
| Swap budget | 0 bytes |
| Service | `hve-coder-jr-llama.service` |

## Ownership and paths

The portable configuration and service contract live in the
`humanvalueexchange/hve-coder-jr` repository:

- `config/llama-cpp.yaml`
- `deploy/bin/start-llama-cpp-jr.sh`
- `deploy/systemd/hve-coder-jr-llama.service`
- `tests/runtime/test_llama_config.py`
- `tests/runtime/test_llama_service_contract.py`

The host deployment environment is:

- Environment: `~/.config/hermes/hve-coder-jr-llama.env`
- Runtime state: `~/.hermes/runtime/hve-coder-jr`
- Logs: `~/.hermes/logs/hve-coder-jr`
- Model root: `/home/hans/models/3rdparty/qwen2.5-coder`

The service is installed in the user systemd manager as a linked unit, but it
is stopped and not enabled. A linked unit is not an activation decision.

## Preflight

Before any start or model replacement:

1. Confirm the profile repository revision and review the diff.
2. Confirm no process is listening on `127.0.0.1:11435`.
3. Confirm the binary is executable and its version/revision is approved.
4. Confirm the exact model file exists.
5. Confirm the SHA256 matches the declared value.
6. Confirm the environment file contains no credentials and has mode `0600`.
7. Confirm Ollama and other HVE services are not being restarted or modified.
8. Confirm the activation approval gate is explicitly open.

The launcher repeats the binary, model existence, and checksum checks at every
startup. A mismatch fails closed before llama.cpp starts.

## Service controls

Inspect without starting:

```bash
systemctl --user status hve-coder-jr-llama.service
systemctl --user is-enabled hve-coder-jr-llama.service
ss -ltn | grep ':11435'
```

The service must remain inactive until the activation evidence packet is
accepted. Starting it is a consequential activation action, not a routine
health check.

The unit enforces or declares:

- Loopback-only binding.
- `MemoryMax=8G`.
- `MemorySwapMax=0`.
- `TasksMax=32`.
- `NoNewPrivileges=yes`.
- `ProtectSystem=strict`.
- `ProtectHome=read-only`.
- Profile-local writable runtime and log paths.
- No automatic restart.

## Validation gates

Validation must proceed in this order:

1. Repository tests and shell syntax checks.
2. Offline temporary launcher load.
3. `/health` returns HTTP 200.
4. `/v1/models` reports the exact approved model ID.
5. A bounded completion succeeds.
6. `/metrics` reports prompt and generated-token counters.
7. Peak process residency is measured against the 8 GiB budget.
8. Memory PSI and swap-in evidence remain acceptable.
9. Concurrent validation confirms resident Ollama models remain loaded and
   unaffected.
10. Controlled timeout/cancellation and recovery evidence is recorded.
11. Luna reviews the evidence and Hans approves activation separately.

The validated temporary load on 2026-09-12 reported HTTP 200 health, the
approved model alias, a successful bounded coding response, prompt and
generation metrics, approximately 6.3 GiB peak RSS, and zero current memory
PSI. This evidence does not by itself activate the service.

## Failure and rollback

If preflight, checksum, readiness, residency, concurrency, or cancellation
evidence fails:

- Stop the temporary or approved process through its known service/process
  boundary.
- Preserve the complete stderr and metrics evidence.
- Do not retry indefinitely or silently change model, context, or budget.
- Leave the service inactive.
- Restore the previous approved profile-owned configuration if a deployment
  change was staged.
- Escalate ambiguous worker or memory state to Luna and Hans.

Do not unload Ollama models, modify the live Hermes-Coder queue, or change
another HVE profile as a recovery action.

## Activation boundary

This runbook establishes a correct, disabled-first llama.cpp foundation. It
does not authorize production activation, external binding, model promotion,
automatic fallback, or changes to Ollama or vLLM. Those actions require a
separate evidence review and explicit human approval.
