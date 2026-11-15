# HVE-CFO Camofox Mortgage Fallback Validation

- **Date:** 2026-11-15
- **Version:** v1.0
- **Status:** Live supervised validation passed; pilot remains active
- **Owner:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Scope:** HVE-CFO `best-mortgage-rate` daily cron job and bounded local Camofox fallback

## Executive status

Hans confirmed that the HVE-CFO daily mortgage-rate cron validation passed after
the Camofox fallback corrections. The job remains a supervised pilot and does
not grant HVE-CFO authority to make binding lender, filing, payment, or other
financial decisions.

The fallback is limited to public lender pages, one bounded Camofox attempt
after a plain-source transport or schema failure, one controlled Outbox write,
and unavailable values when the source cannot be validated.

## Root cause and correction

The first live Camofox attempt failed before page navigation because the
floating `playwright-core` dependency resolved to `1.65.1`, which sent the
`legacyInterceptor` download option that the bundled Camoufox protocol rejected.
The local Camofox runtime was rebuilt with `playwright-core` pinned to `1.58.0`.
The pinned server then returned successful tab creation and navigation.

The next failure was in the cron runner: BMO's plain endpoint returned HTTP 200
with a schema that the lender parser could not interpret. The runner only
invoked Camofox after transport failure or an empty response, so it incorrectly
stopped at the plain response. The runner now invokes Camofox when a fallback
source produces no valid parsed rates, not only when the transport fails.

The BMO adapter also now recognizes the public JSON embedded in a Camofox
accessibility snapshot and preserves the existing validation rules. Invalid,
ambiguous, stale, or unavailable values remain unavailable rather than being
guessed.

## Verification evidence

- The pinned Camofox tab endpoint returned HTTP 200 with successful navigation
  for the public BMO endpoint.
- The exact deployed HVE-CFO environment returned a BMO snapshot and parsed
  valid fixed, variable, and eligible special-rate rows.
- The focused HVE-CFO mortgage suite passed with 28 tests.
- Hans reran Hermes cron job `05ba24ab049a` as `hve-cfo`; the live run
  succeeded and the resulting report was confirmed.
- The scheduled job remains active at `0 16 * * *` in `America/Toronto`.

## Implementation evidence

The HVE-CFO implementation is published on `main`:

- [HVE-CFO `9d8e9bb`](https://github.com/humanvalueexchange/hve-cfo/commit/9d8e9bb)
  — use the local Camofox default endpoint.
- [HVE-CFO `82da216`](https://github.com/humanvalueexchange/hve-cfo/commit/82da216)
  — parse BMO Camofox snapshots.
- [HVE-CFO `d1c5e27`](https://github.com/humanvalueexchange/hve-cfo/commit/d1c5e27)
  — invoke Camofox after a plain-source schema failure.

## Operating boundaries

- Camofox is a local native service; no Docker deployment is part of this
  implementation.
- The Camofox identity is fixed to `hve-cfo-best-mortgage-rate`.
- No cookies, authenticated sessions, personal mortgage data, or personal
  values are sent to the public lender pages or Camofox.
- The Camofox fallback is HVE-CFO skill-local. Fleet-wide standardization
  remains a separate architecture and security decision.
- The pilot remains open until continued scheduled runs provide sufficient
  evidence for a later status review.

