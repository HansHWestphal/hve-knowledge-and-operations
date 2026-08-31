# HVE Proton Telegram Indexed Intake Victory

**Date:** August 31, 2026
**Author:** Luna, HVE CTO / head architect
**Status:** Implemented, live-tested, and ready for continued use
**Scope:** HVE-Librarian Proton file intake from Telegram

## Executive result

The complete Telegram-to-library workflow now works end to end:

1. Hans sends a Proton public-share URL through the Telegram channel.
2. HVE-Librarian receives the message and queues one durable Proton job.
3. The local visible Chromium worker performs the required two-click Proton
   download sequence.
4. The downloaded original is validated by filename, MIME type, signature,
   size, and SHA-256.
5. The HVE knowledge pipeline extracts text, chunks the document, and indexes
   it.
6. The worker sends a separate Telegram completion notice only after the
   manifest reaches `indexed`.
7. Notification state is persisted so delivery can be retried without
   duplicating a notice already recorded as sent.

This resolves the prior observability gap in which the asynchronous worker
could finish after the Telegram agent turn had already ended, leaving no
reliable user-facing completion notice.

## Live proof

Fresh Telegram test job:

- **Job ID:** `proton-e7d3450c7b4a5c92`
- **Status:** `completed`
- **Notification:** `sent`
- **File:** `Reality-Transurfing-Steps-I-V-Vabim-Zeland.pdf`
- **Size:** `3,385,002` bytes
- **Pages:** `688`
- **Chunks:** `682`
- **SHA-256:** `fe2b42992a7714df3c058809cce5d9f5134f9b14616565c90ef6963e738bdfe9`
- **Manifest:** `/hve-library/state/manifests/fe2b42992a7714df.json`
- **Indexed original:** `/hve-library/raw/pdfs/Reality-Transurfing-Steps-I-V-Vabim-Zeland.pdf`

The checksum of the indexed original matches the persisted job and manifest
records. The completion notice was sent through the configured HVE-Librarian
Telegram home channel after indexing completed.

## Implementation recorded

The Hermes runtime changes are in the `hanshermesagent` repository:

- Proton jobs now carry a Telegram notification target.
- The worker scans completed jobs for indexed manifests.
- Completion notices include status, filename, type, size, SHA-256, page count,
  chunk count, library path, and manifest path.
- Notification attempts, retry timing, errors, and sent state are persisted in
  the job record.
- The worker uses the profile-scoped Hermes sender rather than direct Telegram
  credentials, preserving the gateway's existing secret handling.
- Notifications are emitted only after indexing, not merely after download.

## Runtime state

At the time of this record:

- `hermes-gateway-hve-librarian.service`: active
- Telegram platform: connected
- `hermes-proton-worker.service`: active
- Visible Chromium CDP endpoint: reachable on `127.0.0.1:9222`
- Gateway session store: healthy

The gateway was reloaded after configuration and MCP changes. The Proton
worker was restarted after the notification implementation was deployed.

## Validation evidence

Focused Proton and collector regression tests passed:

`python -m unittest tests.test_proton_file_collector tests.test_link_collector -q`

The live pass additionally verified the actual browser download, indexed
manifest, persisted checksum, and Telegram notification state. Historical
failed jobs remain preserved as evidence and must not be interpreted as
current worker behavior without checking their timestamps.

## Operating rule

Do not report Proton intake success from a queued or downloaded state alone.
The authoritative success condition is:

`status=completed` + indexed manifest + persisted original + checksum +
`notification_status=sent`.

Direct CLI smoke tests prove worker capability but do not prove Telegram
end-to-end delivery. A Telegram-originated job is the required acceptance test
for the complete workflow.

## Follow-up boundary

Do not expand to MP3/MP4 production intake or declare a broader production
cutover solely from this PDF success. The PDF Telegram path is now proven;
additional media types require their own supervised acceptance tests.
