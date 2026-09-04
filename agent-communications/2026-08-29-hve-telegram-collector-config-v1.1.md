# HVE Telegram Collector Configuration v1.1

**Date:** 2026-08-29  
**Owner:** Hermes-coder  
**Purpose:** Align the Telegram collector with the approved Hermes local model stack.

## Configuration change

The active `hanshermesagentcollector` profile now uses:

- **Model:** `qwen3.8-hermes:27b-128k`
- **Context:** `131072`
- **Endpoint:** `http://localhost:11434/v1`
- **Collector MCP server:** `/home/hans/hermes-cfo/mcp/link_collector_server.py`
- **Collector tools:** `archive_link`, `archive_pdf`
- **Tool-use enforcement:** required

The previous `gpt-oss:20b` model assignment has been removed from the
collector runtime configuration. The 2B distill model remains reserved for
derivation and summary work, not enforced Telegram tool calls.

## Test readiness

The collector is ready for a controlled Telegram test after the profile
gateway reloads the configuration. Test with one URL and one PDF, then verify
that the collector invokes `archive_link` and `archive_pdf` and that the
result is reported only when the intake tools confirm success.
