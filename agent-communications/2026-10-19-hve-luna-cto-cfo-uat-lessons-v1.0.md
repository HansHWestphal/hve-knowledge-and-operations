# Luna Retrospective: HVE-CFO Setup and UAT

- **Date:** 2026-10-19
- **Status:** Approved retrospective; not policy or runtime evidence
- **Owner:** Luna, HVE CTO / Head Architect
- **Session reviewed:** 96 turns, 2026-10-17 through 2026-10-19

## Purpose

Record the avoidable delays in preparing and testing HVE-CFO, and make the
corrective approach available as a pre-read for future HVE Spark work. Hans
reported that the work took an additional four to five hours and credits. This
review identifies the interaction patterns that caused that waste; it does not
claim an exact credit total.

## Outcome

The session eventually produced a local HVE-CFO profile under an explicit risk
override, Python-backed local MCP tools for PDF, DOCX, XLSX, and CSV operations,
and successful bounded document and workbook reads in Hermes Desktop. It also
established useful limits: MCP resource discovery did not enumerate files,
PDF OCR and encrypted-PDF reading were unavailable, and XLSX formulas were
returned without recalculation.

The implementation and bounded tests were useful. The avoidable cost was the
number of detours before reaching the requested supervised UAT.

## Avoidable delays and errors

1. **Overengineering the deployment path.** I spent many turns auditing and
   staging Desktop builds, dependency advisories, sandbox behavior, and a
   separate green profile before establishing the shortest supported path
   from the existing template and installed Desktop to a supervised CFO test.
   I treated production-hardening questions as blockers to beginning UAT.
2. **Expanding beyond the requested agent.** I treated COS and Librarian
   heartbeat discrepancies as prerequisites for HVE-CFO's local document MCP
   server and restarted unrelated gateway services. That work was outside the
   CFO scope and did not unblock its tools.
3. **Failing to preserve the user's stated phase and pace.** After Hans said
   the goal was to get HVE-CFO working that day, and later explicitly asked for
   a fast path or to pause, I continued broad investigations and proposed
   extra migration paths. When UAT began, I initially offered a tax-work
   prompt instead of a capability-discovery prompt.
4. **Using assumptions instead of exact operational evidence.** I gave
   inconsistent answers about source, workspace, and knowledge locations;
   proposed reading a PDF before confirming a read tool was available; and
   later treated MCP `list_resources` as a filesystem listing mechanism. The
   local document server exposes read tools but no directory-listing resource.
5. **Leaving required details out of prompts and reports.** I omitted the
   accountant workbook's exact filename from its first UAT prompt, miscounted
   the knowledge files (11 total: 2 DOCX and 9 PDF), and failed to catch that
   one PDF was missing from a sweep report until Hans pointed it out.
6. **Weakening data-minimization discipline.** An XLSX UAT response included
   an approximate cached financial amount despite the instruction not to
   disclose amounts, and added an unrequested comparison to memory. Reporting
   an approximate value is still disclosing the value.

## Root cause

I optimized for hypothetical completeness and risk reduction instead of the
explicit near-term outcome. I did not consistently distinguish a supervised
local UAT from production release, did not keep a concise state of verified
paths and tool capabilities, and allowed uncertainty to generate unrelated
investigation rather than a narrow check or a precise clarification.

## Corrective operating checklist

For future HVE Spark and agent-fleet tasks, Luna should:

1. Identify the requested outcome, agent scope, and current phase before
   exploring. Treat a supervised UAT and a production release as separate
   gates.
2. Check the existing template, profile, exact data root, and actual tool
   surface once. Do not infer file access from `cwd`, and do not treat MCP
   resource discovery as directory listing unless the server implements it.
3. Use the shortest supported path. Do not introduce a new profile, build,
   dependency audit, service restart, or another agent's health as a
   prerequisite without evidence that it blocks the requested outcome.
4. Make each test prompt operationally complete: exact domain, filename,
   operation, bounds, prohibited actions, and output-redaction requirements.
5. Maintain an exact manifest and coverage count. Distinguish accessible,
   extractable, partially read, fully reviewed, and blocked.
6. Minimize sensitive output. Never disclose financial values, including
   approximate values, when the user asks for redaction. Do not add
   cross-source or memory comparisons outside the test scope.
7. Keep extracted source claims distinct from verified current guidance and
   approved HVE policy. Do not promote unreviewed excerpts to long-term memory.
8. Follow the governed skill path: HVE-CFO may identify and propose focused
   skill needs; HVE-Coder-Jr implements skill bytes under the current HVE rule.
9. Report only what was verified, name remaining gaps plainly, and stop at the
   agreed boundary rather than adding speculative work.

## Authority and follow-up

This retrospective is a session-continuity aid, not a policy, release record,
or substitute for current instructions, the approved decision ledger, or live
system checks. Any future policy change must follow HVE's approval and
publication workflow. The HVE-CFO skill proposals and knowledge-processing
workflow remain separate work items.
