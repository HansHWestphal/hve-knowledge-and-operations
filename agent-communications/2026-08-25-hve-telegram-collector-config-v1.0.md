# HVE Telegram Collector Configuration v1.0

**Date:** 2026-08-25  
**Owner:** Hermes-coder  
**Purpose:** Record the restored functional Telegram link/PDF collector configuration.

## Current configuration

- **Telegram chat:** `1477642616`
- **Primary routed profile:** `hanshermesagentcollector`
- **Collector profile model:** `gpt-oss:20b` via local Ollama
- **Collector MCP server:** `/home/hans/hermes-cfo/mcp/link_collector_server.py`
- **Collector tools:** `archive_link`, `archive_pdf`
- **Durable intake root:** local HVE knowledge library
- **Gateway:** `hermes-gateway-hanshermesagent.service`
- **Multiplex routing:** enabled

The collector profile remains the strict Telegram ingestion surface. Its identity and operating rules are defined in `~/.hermes/profiles/hanshermesagentcollector/SOUL.md`.

## Corrective alignment

The active `hanshermesagent` fallback configuration had `hve-link-collector` listed as disabled while also referencing it from the Telegram toolset. That produced the runtime warning that Telegram had no valid toolsets and could lead to invalid tool calls.

The fallback configuration is now aligned with the functional collector release:

- `hve-link-collector` is enabled.
- `archive_link` and `archive_pdf` are exposed to Telegram.
- The stale `disabled_toolsets` entry is removed.
- The explicit Telegram route to `hanshermesagentcollector` is preserved.

No credentials or tokens are recorded here.
