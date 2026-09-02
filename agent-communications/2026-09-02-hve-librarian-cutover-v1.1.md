---
title: HVE-Librarian Official Collector Retirement
status: approved-operational-record
owner: Hans Westphal
effective_date: 2026-09-02
---

# HVE-Librarian Official Collector Retirement

## Decision

`hanshermesagentcollector` is officially retired from live operations.
HVE-Librarian has taken over full librarian duties for the HVE knowledge
layer and is the sole live Telegram intake profile for knowledge archival.

## HVE-Librarian responsibilities

HVE-Librarian now owns:

- link archival;
- YouTube source and transcript intake;
- native Telegram PDF archival;
- Proton fallback for oversized Telegram files;
- extraction, chunking, indexing, retrieval, and validation;
- provenance, deduplication, and failure reporting;
- knowledge-layer stewardship and archival communications.

## Runtime state

- `hermes-gateway-hve-librarian.service` remains the active Telegram gateway.
- `hermes-gateway-hanshermesagentcollector.service` is not present or active.
- `hermes-proton-worker.service` remains active as HVE-Librarian's asynchronous
  Proton processing backend.
- The former collector profile remains preserved locally for a limited rollback
  period and is not connected to live Telegram routing.

## Rollback posture

The collector profile will remain available temporarily while HVE-Librarian's
live operation is observed. It must not be started concurrently with
HVE-Librarian. Any rollback requires stopping HVE-Librarian's Telegram gateway,
restoring the previously documented routing, and recording a new approved
operational decision.

## Status

The retirement and ownership transfer are complete. Profile deletion is
deferred until the rollback observation period concludes.
