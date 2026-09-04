# HVE Telegram Collector Configuration v1.2

**Date:** August 30, 2026
**Status:** Approved superseding clarification
**Supersedes:** `2026-08-29-hve-telegram-collector-config-v1.1.md`

## Current configuration

The active `hanshermesagentcollector` profile remains the live Telegram
ingestion surface until `hve-librarian` passes validation and Hans approves
cutover.

The current collector capability set includes:

- `archive_link`
- `archive_youtube`
- `archive_pdf`

YouTube archiving was added in the later August session work and supersedes the
incomplete capability list in v1.1. Historical configuration records remain
preserved.

## Migration boundary

No collector capability, channel route, historical record, or production
workflow is retired until replacement coverage, safety validation, routing
verification, rollback steps, and explicit Hans approval are recorded.
