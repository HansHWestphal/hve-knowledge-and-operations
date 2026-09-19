# HVE Spark Shared Infrastructure — Tailscale, Ollama, and vLLM

**Date:** September 18, 2026  
**Status:** Current shared-infrastructure reference  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision owner:** Hans Westphal

## Purpose

This document records the shared Spark infrastructure boundary for the
networking and inference services that support HVE agents. Tailscale, Ollama,
and vLLM are platform services; individual agent profiles consume them but do
not own or reconfigure them independently.

## Shared services

| Service | Current boundary | Purpose | Ownership |
|---|---|---|---|
| **Tailscale** | `tailscaled.service`; Spark tailnet address `100.85.145.63` | Private HVE mesh connectivity and controlled HTTPS ingress for approved services | Shared Spark infrastructure; Luna governs architecture |
| **Ollama** | `ollama.service`; `127.0.0.1:11434` | Shared local model serving for HVE agent workloads | Shared Spark infrastructure |
| **vLLM coder runtime** | `hve-coder-runtime.service`; `127.0.0.1:11435` | Shared serialized coder inference for HVE-Coder-Jr and HVE-Coder-Sr | Shared Spark infrastructure; Jr/Sr remain profile-separated |

## Tailscale operating model

Tailscale provides:

- Encrypted private connectivity between approved HVE devices
- Stable Spark tailnet addressing
- HTTPS Serve/Funnel capability for explicitly approved service boundaries
- A shared transport layer without exposing inference services directly to the
  public internet

The Spark currently has an active Tailscale node and a public Funnel route for
the legacy HVE-CFO MCP service. That route must not be repurposed for another
service without an explicit routing decision.

## Current and retired route

The former route was:

```text
https://spark-5054-1.tail3b0306.ts.net/
  -> 127.0.0.1:8765
  -> legacy hve-cfo MCP server
```

The legacy CFO MCP service was stopped and disabled on September 18, 2026. Its
public Funnel route was removed after the service shutdown. Its future rebuild
belongs to the new template-derived HVE-CFO fleet instance. The Tailscale node
itself remains active for shared infrastructure and must not be stopped as part
of the CFO decommission.

## Invariants

1. Ollama remains on `127.0.0.1:11434`.
2. The shared vLLM coder runtime remains on `127.0.0.1:11435`.
3. Tailscale configuration changes must preserve existing shared routes and
   require explicit service-by-service verification.
4. Agent profiles must not stop, reconfigure, or repurpose shared Tailscale,
   Ollama, or vLLM services as part of ordinary profile work.
5. Public exposure requires an authenticated application boundary, a named
   owner, a documented purpose, health evidence, and a rollback command.
6. Retiring an agent service must remove its public route and stop its local
   listener without removing the shared Tailscale node.

## Verification commands

```bash
tailscale status
tailscale serve status
tailscale funnel status
systemctl status ollama.service
systemctl status hve-coder-runtime.service
ss -ltnp | grep -E ':(11434|11435)\b'
```

Do not include API keys, tailnet authentication material, SMTP secrets, model
credentials, or runtime state in GitHub artifacts.
