# HVE Proton Intake Worker Handoff

**Date:** August 31, 2026  
**Author:** Luna, HVE CTO / head architect  
**Audience:** Luna / next technical session  
**Status:** Draft handoff for continuation; not a production cutover decision

## Purpose

This handoff records the exact state of the HVE-Librarian Proton intake work
after supervised browser and Telegram testing. It exists to prevent the next
session from conflating direct worker smoke tests, Telegram queueing, and
background worker processing.

## Governing user correction

Hans explicitly defined the required Proton UI behavior:

1. Wait until the Proton PDF page and viewer are fully loaded.
2. Click the top **Download** button beside **Save for later** once.
3. Move the pointer slightly.
4. Click the **Download** item in the opened menu.
5. Wait for the browser transfer to complete before staging the file.

The worker must prove both clicks and the completed transfer. Rendering a page,
creating a queue record, or observing a browser notification is not intake
success.

## Repository and runtime locations

- Hermes runtime worktree: `/home/hans/hanshermesagent`
- Proton collector: `/home/hans/hanshermesagent/tools/proton_file_collector.py`
- Collector MCP server: `/home/hans/hanshermesagent/mcp/link_collector_server.py`
- Proton collector tests: `/home/hans/hanshermesagent/tests/test_proton_file_collector.py`
- Librarian profile: `/home/hans/.hermes/profiles/hve-librarian`
- Durable HVE library: `/hve-library`
- CDP endpoint: `http://127.0.0.1:9222`
- Visible Chromium profile: `/home/hans/.hermes/profiles/hanshermesagent/cache/cdp-browser`

Do not expose Proton access fragments, credentials, or complete private share
URLs in messages or durable notes.

## Verified successful direct smoke test

A direct CLI worker smoke test succeeded after the two-click implementation was
corrected. The visible browser loaded the recorded Proton PDF, performed the
two-click interaction, and completed the transfer.

Successful job:

- Job ID: `proton-16b56f0802a62a6d`
- Status: `completed`
- File:
  `/hve-library/intake/inbox/InnovationThroughAnalytics-MicrosoftWhitePaper.pdf`
- Size: `3829249` bytes
- Manifest:
  `/hve-library/state/manifests/1c5a907fbc25cd14.json`
- SHA-256:
  `1c5a907fbc25cd14eb9deb00a2aa6a76b73a43f66322a4fef1fcfa119d2af017`

This proves the corrected worker can perform a real Proton download when
invoked directly. It does not, by itself, prove the Telegram-to-worker
end-to-end path.

## Current worker implementation

`_download_via_browser()` now:

- Creates a CDP target through `/json/new`.
- Enables Page and Network domains.
- Brings the target to the front.
- Enables browser download behavior with a temporary download directory.
- Navigates to the canonical Proton URL.
- Waits for `document.readyState === "complete"` and the visible
  `data-testid="dropdown-download-button"` control.
- Obtains the top control coordinates.
- Uses `Input.dispatchMouseEvent` for a real mouse move, press, and release.
- Moves the pointer by a small offset.
- Waits for a second visible exact-text **Download** menu item.
- Uses real CDP mouse events to click the menu item.
- Waits for browser download events and a completed file.
- Verifies non-empty file size, MIME, filename, signature, checksum, and
  atomic staging.

Failure messages are now phase-specific:

- Proton PDF did not finish loading or its top Download button was unavailable.
- Proton top Download click did not open the download menu.
- Proton menu Download item did not become clickable.
- Proton menu Download click produced no completed browser download.

The worker also corrected a CDP response-shape bug: `Runtime.evaluate` returns
the value at `result.value`, not `result.result.value`.

## Current Telegram state

The Librarian Telegram gateway is healthy and polling. The latest Telegram
test message was received and caused `archive_proton_file` to create:

- Job ID: `proton-58c2cb39ed4b85aa`
- Status at handoff: `queued`

The job has not been downloaded because the Proton worker service is currently
stopped. Telegram queueing and Proton processing are separate stages.

The Librarian session also made an unnecessary `archive_link` call after the
Proton call. This is routing noise and should be corrected, but it did not
prevent the Proton job from being queued.

Earlier in the session, one Telegram turn caused repeated
`archive_proton_file` calls. Protections were added:

- Proton results include `retryable: false`.
- Results include an explicit no-retry agent action.
- Collector MCP instructions say to call `archive_proton_file` at most once per
  user request.
- The Librarian profile system prompt says Proton results are terminal and
  must not be retried.

These prompt/config changes require the Librarian gateway to reload before
their runtime effect can be assumed.

## Worker service state

The user explicitly requested the Proton worker be stopped during debugging.
It was stopped with:

`systemctl --user stop hermes-proton-worker.service`

Current verified state at handoff:

- `hermes-gateway-hve-librarian.service`: active
- `hermes-proton-worker.service`: inactive

Do not describe the Telegram test as complete until the worker is deliberately
restarted and the queued job reaches a persisted terminal state.

## Tests already run

The focused collector tests passed after the two-click implementation:

`python -m unittest tests.test_proton_file_collector tests.test_link_collector -v`

These tests validate the mocked sequence and collector behavior. They do not
replace the supervised visible-browser smoke test or the Telegram end-to-end
test.

## Known historical failures

Older jobs remain in `/hve-library/state/jobs/` and are preserved as evidence.
They include failures for:

- Incorrect one-click/two-click logic.
- Missing menu detection.
- Incorrect CDP `Runtime.evaluate` response interpretation.
- A stale worker job that was intentionally not retried.

Do not treat those historical failures as current worker behavior without
checking the job timestamp and code version.

## Exact continuation sequence

1. Confirm the current visible CDP browser is still running on port `9222`.
2. Confirm the Librarian gateway has reloaded the latest MCP instructions and
   tool code.
3. Start `hermes-proton-worker.service`.
4. Observe job `proton-58c2cb39ed4b85aa` without exposing its URL.
5. Require the visible browser to show the loaded Proton PDF, top Download
   click, pointer movement, menu Download click, and completed transfer.
6. Require the job to contain `status: completed`, `source_path`,
   `manifest_path`, file size, and SHA-256.
7. Only after that, report the Telegram end-to-end test as successful.
8. If the worker fails, preserve the job and capture the exact phase-specific
   error before changing selectors or timing.
9. Do not move to MP3/MP4 or production cutover until the Telegram PDF path is
   proven.

## Session discipline

Keep these states separate in every report:

- **Direct smoke:** worker invoked manually from the CLI.
- **Telegram intake:** Telegram message received and a durable job queued.
- **Worker processing:** background service actively downloading a queued job.
- **Completed intake:** staged original, manifest, checksum, and persisted
  terminal status.

Never claim end-to-end success from a queued job alone. Never restart or stop
the worker silently; record the state transition and reason.
