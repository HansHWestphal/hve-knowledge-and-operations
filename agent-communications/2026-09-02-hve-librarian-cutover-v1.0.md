---
title: HVE-Librarian Final Telegram Cutover
status: approved-operational-record
owner: Hans Westphal
effective_date: 2026-09-02
---

# HVE-Librarian Final Telegram Cutover

## Decision

HVE-Librarian is now the final live Telegram intake profile for HVE knowledge
archival. `hanshermesagentcollector` is retired from live routing and remains
preserved locally as a rollback asset.

## Scope

HVE-Librarian owns the validated evidence workflow:

- link archival;
- YouTube source and transcript intake;
- native Telegram PDF archival;
- Proton fallback for oversized Telegram files;
- extraction, chunking, indexing, retrieval, validation, and failure reporting;
- provenance and duplicate handling.

The existing `hermes-proton-worker.service` remains active. It is shared
backend infrastructure for asynchronous Proton processing, not a second
Telegram profile and not part of the retired collector gateway.

## Evidence

- `hermes-gateway-hve-librarian.service` is enabled and active.
- Its Telegram platform is connected for Hans's approved home channel.
- HVE-Librarian has the collector and read-only knowledge-library MCP servers
  registered.
- No `hermes-gateway-hanshermesagentcollector.service` exists or is active.
- The former collector profile remains at
  `/home/hans/.hermes/profiles/hanshermesagentcollector`.
- Proton intake remains served by `hermes-proton-worker.service`.
- End-to-end Proton indexing was recorded in
  `hve-librarian/docs/2026-08-31-proton-telegram-indexed-intake-victory.md`.

## Rollback

Rollback is reversible while the preserved collector profile and intake code
remain available. Stop or disable the HVE-Librarian gateway, restore the
collector routing configuration, and start the collector gateway only after
confirming that HVE-Librarian is no longer connected to the Telegram channel.
Do not run both Telegram intake gateways simultaneously.

## Status

The cutover is complete. Future changes to Telegram ownership, retirement, or
rollback require a new approved operational record.
