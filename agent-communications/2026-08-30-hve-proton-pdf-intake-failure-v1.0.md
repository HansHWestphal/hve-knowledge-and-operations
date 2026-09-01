# Proton Drive PDF Intake Failure — Evidence Note

**Date:** 2026-08-30 (job ran 2026-08-31 03:10–03:11 UTC / 2026-08-30 23:10–23:11 EDT)
**Author:** HVE-Librarian (knowledge-intake profile)
**Requested by:** Hans Westphal (re-test)
**Status:** Failure confirmed; no file archived, nothing indexed

## Result

- Job ID: `proton-f270db7e45b1c7bf`
- URL: [redacted Proton share URL; retained in the private job record]
- Error: `ProtonFileCollectorError: No Proton download menu was found`
- Worker ran, exited ~1 minute later: `archived: false`, `indexed: false`, `source_path: null`, `manifest_path: null`
- This is a repeat failure (same error class as the earlier attempt).

## Interpretation (not yet verified)

Two candidate causes, in order of likelihood:

1. **Share is private / login-gated** — if the Proton Drive file is not shared as "Anyone with the link", the page renders an auth screen and no download menu exists for the collector to find. Hans should verify in Proton Drive (file → Sharing).
2. **Collector selector/flow broken** — if the link opens fine in a logged-out browser, the Proton scraper in the intake worker no longer matches Proton's page structure and needs a fix (Luna / Technical Architect lane).

## Decision required

- **A)** Hans flips the share setting to "Anyone with the link" (view) → Librarian re-queues the job.
- **B)** If the link opens fine without login → route to Luna as a collector defect; this note + job ID are the evidence.

## Provenance

- Source: HVE link-collector MCP tool `archive_proton_file`, job record `proton-f270db7e45b1c7bf`.
- This file is a note/evidence record only. It does not constitute policy, a decision, or endorsement of any content in the PDF.
- No PDF content was captured or copied.
