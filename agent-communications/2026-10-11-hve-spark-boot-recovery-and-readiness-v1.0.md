# HVE Spark Boot Recovery and Startup Readiness

**Date:** 2026-10-11
**Version:** 1.0
**Prepared by:** Luna, HVE CTO / Head Architect
**Decision authority:** Hans Westphal, CEO
**Status:** Recovery actions and startup hardening implemented; reboot validation pending
**Scope:** DGX Spark boot incident, Hermes messaging gateways, Ollama preload, and shared vLLM startup

## 1. Executive summary

The DGX Spark (`spark-5054`) experienced an unscheduled reboot on October 11,
2026. The current boot began at approximately 07:54 EDT. Available evidence
does not establish what triggered the reboot.

The principal service gap was HVE-COS's WhatsApp gateway: its prior process
ended uncleanly with the VM, and its user service was disabled, so it did not
return automatically. The gateway was subsequently enabled and started.
HVE-Librarian's Telegram gateway remained the Telegram owner.

Boot logs also showed vLLM failing one startup attempt because insufficient KV
cache was available for the required 65,536-token context. systemd retried and
vLLM became healthy. HVE-Coder-Jr attempted to connect before the vLLM API was
ready and restarted repeatedly before recovering.

Hans selected readiness/order gates while preserving the existing vLLM memory
budget and 65,536-token context. Those changes were implemented and pushed to
the owning repositories. No vLLM restart or Spark reboot was performed.

## 2. Incident and recovery evidence

### Reboot

- The current boot began at approximately **07:54 EDT, October 11, 2026**.
- No retained evidence identified a kernel panic, OOM event, thermal event,
  GPU fault, storage failure, or package update as the cause.
- Kdump is installed but disabled and not ready; no crash dump was available.
- **Conclusion:** reboot cause remains unknown. Startup overlap may have
  contributed to inference-service startup pressure, but it is not evidence
  of what caused the host reboot.

### Gateway recovery

- The prior HVE-COS gateway process had a heartbeat shortly before the reboot
  and was recorded on its next startup as having exited uncleanly with the VM.
- The HVE-COS profile-specific user service was inactive and disabled. It was
  enabled and started without replacing its unit or affecting other profiles.
- The WhatsApp bridge reconnected and the gateway recorded a fresh heartbeat.
  No test message was sent.
- HVE-Librarian's Telegram gateway remained active and enabled.
- No generic gateway, retired profile, or `--all` gateway action was used.

### Inference startup

- Ollama preload and vLLM initialization ran concurrently at boot.
- vLLM's first launch had 2.52 GiB available for KV cache, below the 3.5 GiB
  required for the configured 65,536-token context. Its systemd restart policy
  retried; a subsequent launch succeeded with 6.14 GiB of cache.
- HVE-Coder-Jr connected before the vLLM API became ready, received connection
  refusals, and restarted repeatedly before becoming active.
- The sequence is consistent with a readiness race and resource contention,
  but does not prove that preload caused the initial vLLM failure.

## 3. Implemented startup hardening

The chosen approach preserves `gpu_memory_utilization: 0.10`, the existing
approximately 12 GiB vLLM budget, and `max_model_len: 65536`.

1. **Ollama model preload:** added a user-systemd drop-in that waits up to five
   minutes for the vLLM health endpoint before GPU-heavy model warmup. If the
   wait expires, preload continues so Ollama is not left cold. The live drop-in
   is loaded; the completed preload service was not restarted.
2. **Shared runtime readiness:** added `wait_for_runtime` to the shared
   `hve-coder-runtime` package. It retries transient connection failures,
   timeouts, and retryable HTTP responses within a bounded startup window;
   invalid model identity and other contract errors fail immediately. Each
   readiness attempt is bounded by the remaining deadline.
3. **Coder-Jr startup:** the supervisor waits for shared vLLM health and the
   pinned model identity before starting its worker, instead of treating the
   systemd process-active state as API readiness.
4. **Session continuity:** added session-bootstrap guidance to the knowledge
   repository's `AGENTS.md`, directing future sessions to repository context,
   current role/decision sources, relevant operational handoffs, and live
   service/profile/channel checks.

The shared-runtime suite passed **12 tests**. Python syntax and whitespace
checks passed. The readiness helper also verified the live vLLM health
endpoint and pinned model identity.

## 4. Repository records

- Knowledge repository session-bootstrap guidance: commits
  [`ea72315`](https://github.com/HansHWestphal/hve-knowledge-and-operations/commit/ea72315)
  and [`63bf126`](https://github.com/HansHWestphal/hve-knowledge-and-operations/commit/63bf126).
- HVE-CFO preload drop-in template and mapping:
  [`a01def8`](https://github.com/humanvalueexchange/hve-cfo/commit/a01def8).
- Shared runtime bounded readiness helper and tests:
  [`248d388`](https://github.com/humanvalueexchange/hve-coder-runtime/commit/248d388).
- HVE-Coder-Jr readiness integration and supervisor documentation:
  [`c5546dc`](https://github.com/humanvalueexchange/hve-coder-jr/commit/c5546dc).

## 5. Current state and boundaries

At the final service check for this report, the following were active and
enabled:

- System services: Ollama, shared vLLM runtime, HVE-Coder-Jr, and Open WebUI.
- User services: Hermes model preload, HVE-COS WhatsApp gateway, and
  HVE-Librarian Telegram gateway.

The preload readiness drop-in is in effect for future starts. The Coder-Jr
readiness code is pushed, but its running process was not restarted to load the
new code. The next Coder-Jr service start will use it.

No shared vLLM restart, host reboot, test WhatsApp message, or forced Hermes
gateway reinstall/deployment was performed. HVE-CFO's unrelated pre-existing
script edits were left untouched and uncommitted.

## 6. Open follow-up

- Keep the reboot cause classified as **unknown** unless new diagnostic
  evidence becomes available. Investigate DGX-supported power, firmware, and
  crash diagnostics separately; review kdump feasibility before enabling it.
- At an approved maintenance window, perform a controlled reboot and verify
  service ordering, model readiness, profile-specific gateway enablement, and
  channel reconnection. A successful controlled reboot will validate startup
  behavior, not explain the earlier reboot.
- Investigate the Hermes release-controller status failure before any forced
  gateway-unit refresh or deployment.
- Preserve the 64K context floor and current vLLM memory budget unless Hans
  approves a new measured configuration.
