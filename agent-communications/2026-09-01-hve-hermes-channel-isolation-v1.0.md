# HVE Hermes Channel Isolation Configuration

**Date:** 2026-09-01  
**Owner:** Luna, HVE Head Architect and CTO  
**Status:** Approved operational record  
**Repository:** `HansHWestphal/hve-knowledge-and-operations`

## Purpose

This record documents the completed separation of Hermes messaging channels on
the DGX Spark. The configuration is intentionally machine-local: the runtime
files remain under `/home/hans/.hermes` and `/home/hans/.config/systemd/user`;
this repository records the approved operating state and evidence without
copying credentials, session data, or runtime state.

## Approved channel ownership

| Profile | Primary channel | Disabled channel | Gateway mode |
|---|---|---|---|
| `hanshermesagent` | WhatsApp | Telegram | Independent single-profile gateway |
| `hve-librarian` | Telegram | WhatsApp | Independent single-profile gateway |

The profiles no longer share messaging-channel ownership. HVE-Librarian
operates independently on Telegram, while Hans Hermes communicates through the
preserved WhatsApp session.

## Implemented configuration

### Hans Hermes profile

The active file is
`/home/hans/.hermes/profiles/hanshermesagent/config.yaml`.

- Telegram is explicitly disabled.
- The Hans Telegram `gateway.profile_routes` entry was removed.
- `gateway.multiplex_profiles` is set to `false`, preventing Hans from loading
  HVE-Librarian or other secondary profiles into its gateway process.
- WhatsApp remains enabled with the existing Hans home channel.
- The existing WhatsApp authentication/session directory was preserved.

### Hans systemd service

The active drop-in is
`/home/hans/.config/systemd/user/hermes-gateway-hanshermesagent.service.d/override.conf`.

- Hans starts with `gateway run` and no longer uses `--replace`.
- Future Hans restarts therefore cannot forcibly take ownership of the shared
  Telegram bot token.

### HVE-Librarian profile

The active file is
`/home/hans/.hermes/profiles/hve-librarian/config.yaml`.

- Telegram remains enabled.
- Librarian runs as its own gateway process and owns the Telegram connection.

## Validation evidence

The final verification on 2026-09-01 confirmed:

- `hermes-gateway-hanshermesagent.service`: active.
- `hermes-gateway-hve-librarian.service`: active.
- Hans WhatsApp health: `status=connected`, `queueLength=0`.
- HVE-Librarian Telegram state: connected.
- No Telegram token-lock, token-handoff, or Telegram initialization errors
  appeared after the final isolation restart.
- Hans cron execution completed successfully at
  `2026-09-01T09:21:39-04:00`.
- The repository worktree contained no changes from the runtime operation.

A transient WhatsApp bridge connection error occurred during the service
restart at 09:04:34; systemd restarted the gateway and the bridge subsequently
returned to `connected` state. No recurring failure was observed.

## Runtime-state note

Hans' `gateway_state.json` retains stale historical Telegram and
`served_profiles` entries from the former multiplexed configuration. These
entries are not treated as active ownership: the current Hans process is
single-profile, initializes WhatsApp only, and does not emit Telegram
initialization or token-lock messages. The runtime state file was not manually
deleted or rewritten.

## Operational boundaries

- Hermes local memory remains SQLite-based; Honcho is not part of this channel
  configuration.
- WhatsApp credentials, session files, Telegram tokens, and other secrets are
  excluded from this record.
- This document records technical operating state and does not create new HVE
  financial, legal, product, or publication policy.
