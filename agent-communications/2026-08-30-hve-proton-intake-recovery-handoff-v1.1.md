# HVE Proton Intake Recovery Handoff

**Date:** 2026-08-30  
**Author:** Luna, HVE CTO / head architect  
**Audience:** HVE-Librarian, Luna, future technical session  
**Status:** Active recovery handoff; Proton intake remains unvalidated

## Executive summary

The relogin/browser-state issue must be resolved before another Proton intake
test. The complete saved Proton URL still opens a rendered PDF page through the
local Chromium CDP endpoint, but the worker has not completed a download,
staged a file, or written a manifest.

The runtime collector was updated in `/home/hans/hanshermesagent` with a
one-shot text-based menu-item lookup and a bounded five-second post-navigation
settle. Its focused 13-test suite passes, but three controlled live worker
attempts still failed before transfer completion. Do not claim success or ask
for another Telegram capture until the browser session has been re-established
after relogin.

## Confirmed findings

- The saved complete URL includes the required access fragment; it was preserved
  through queueing and browser navigation. The fragment is not repeated here.
- The live page title and body render the expected PDF share page and show a top
  **Download** control.
- Before opening the menu, the top control is
  `data-testid="dropdown-download-button"`.
- After one top-control click, Proton renders a second visible **Download**
  button. The live DOM observed both `data-testid="download-button"` and a
  fallback text-only match; selector assumptions must remain bounded and
  one-shot.
- The native desktop Save dialog was not available to this CLI session:
  `xdotool` and `wmctrl` were unavailable, and no physical **Save** click was
  performed.
- The worker service is active as the user service
  `hermes-proton-worker.service`; its earlier import-path restart loop is no
  longer the current failure.
- The final controlled job
  `proton-7e97d5dad53c59f6` ended `failed` with
  `Proton download controls did not complete their one-shot sequence`.
  No `source_path`, `manifest_path`, or SHA-256 was produced.

## Runtime changes made but not yet committed

- `tools/proton_file_collector.py`: one-shot second-button lookup based on
  visible exact text, followed by a bounded five-second page settle after
  `Page.navigate`.
- `tests/test_proton_file_collector.py`: regression coverage for the one-shot
  text lookup and transaction ordering.
- Focused result: 13 Proton collector tests passed.

The runtime worktree contains other unrelated uncommitted changes. Do not
commit or revert them blindly; inspect and separate the Proton changes first.

## Next-session recovery sequence

1. Relogin to the browser/profile used by the Proton share and restore clipboard
   access. Confirm the complete URL can be pasted without removing its `#`
   fragment.
2. Open the saved share manually and verify the page is not login-gated.
3. Use the browser UI to perform exactly one top **Download** click, then one
   menu **Download** click, and complete the native **Save** action if Chrome
   presents it. Do not repeat clicks.
4. Inspect the resulting browser download location and CDP events. Distinguish
   a UI save from a transfer-history entry.
5. If the manual download succeeds, run one worker test against the complete
   URL and require: one job, one transfer, one staged file, one manifest, and a
   matching SHA-256.
6. If manual download succeeds but the worker fails, capture the exact
   `Runtime.evaluate` exception and browser event sequence before changing
   selectors again.
7. If manual download is login-gated, fix the Proton share access setting first;
   do not alter the worker to bypass authentication.

## Session discipline

Keep queueing separate from browser execution and report only persisted states:
`queued`, `in_progress`, `completed`, `duplicate`, `cancelled`, or `failed`.
No page rendering, menu opening, browser notification, or queued job is intake
success. Success requires a staged file, manifest, and verifiable content hash.
