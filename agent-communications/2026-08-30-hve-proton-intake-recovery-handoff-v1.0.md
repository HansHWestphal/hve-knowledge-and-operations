# HVE Proton Intake Recovery Handoff

**Date:** 2026-08-30  
**Author:** Luna, HVE CTO / head architect  
**Audience:** HVE-Librarian, Luna, future technical session  
**Status:** Active recovery handoff; Proton intake is not validated

## Executive summary

The Proton PDF intake experiment remains incomplete. The PDF renders correctly
in Brave when the complete Proton share URL is opened manually, but automated
intake has not yet completed one controlled download into `/hve-library`.
Several iterations consumed time and tokens because browser interaction changes
were declared ready before an isolated live worker test proved one menu-open,
one download-click, and one completed transfer.

The next session must stop treating the current implementation as validated.
Restore or re-establish the previously reliable browser interaction first, then
wrap it with queueing and idempotency without changing its click behavior.

## Confirmed evidence

- Proton uses a browser-rendered share page.
- The supplied PDF page visibly contains a top **Download** control.
- Clicking the top control opens a menu containing a second **Download** item.
- The access fragment after `#` is required for this share and must never be
  removed from the browser URL.
- A handoff once created a job with the fragment removed, which opened the
  wrong/password-gated path.
- Multiple browser transfer entries were observed during an earlier test.
- `/stop` was used to terminate the Librarian session when repeated attempts
  continued.
- No Proton PDF has been accepted into the HVE intake queue or indexed from
  this experiment.

## Relevant job evidence

- `proton-f270db7e45b1c7bf`: failed before the selector correction with
  `No Proton download menu was found`.
- `proton-4f40ec863427acb4`: diagnostic job created with the access fragment
  missing; it was not a valid Proton share handoff.
- `proton-5990eac3ee61495d`: live worker smoke test after the worker refactor;
  failed with `No Proton download menu was found`.

The full Proton access key is intentionally not repeated in this note.

## Current runtime state

- Runtime repository: `/home/hans/hanshermesagent`
- Knowledge library: `/hve-library`
- CDP endpoint: `http://127.0.0.1:9222`
- Worker service: `hermes-proton-worker.service`
- Telegram gateway: `hermes-gateway-hve-librarian.service`
- The gateway and worker were last started after the one-shot refactor, but
  no successful live Proton archive has been proven.
- Do not ask Hans for another Telegram test until the local browser path passes
  without repeated clicks.

## Recovery requirements

1. Preserve the complete Proton URL, including its access fragment, from
   Telegram tool input through the queued job and browser navigation.
2. Reject a fragment-less `drive.proton.me/urls/` share unless a previously
   recorded complete URL for the same share can be recovered safely.
3. Use one browser transaction with explicit one-shot state:
   wait for the top Download control, click once, wait for the menu Download
   item, click once, then stop evaluating click scripts.
4. Track one CDP download event and one expected filename. Never scan all files
   in a shared/default Downloads directory and never infer success from a
   browser transfer-history entry.
5. Keep enqueueing separate from browser execution. The Telegram tool should
   return one durable job ID immediately; a worker should process that job once.
6. Add URL and content-hash idempotency, stale-job recovery, cancellation, and
   terminal failure states before exposing another live test.
7. Validate locally with a fake CDP sequence and then run exactly one live worker
   test. Success requires one job, one transfer, one staged file, one manifest,
   and a verifiable SHA-256.

## Session discipline

Do not claim Proton intake success from page rendering, a queued job, or a
browser download notification alone. Report each state separately:
`queued`, `in_progress`, `completed`, `duplicate`, `cancelled`, or `failed`.
If a browser action must be retried, the retry belongs to the bounded worker,
not to the Librarian model or Telegram conversation.
