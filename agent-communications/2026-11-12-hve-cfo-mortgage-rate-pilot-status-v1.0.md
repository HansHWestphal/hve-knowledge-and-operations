# HVE-CFO Mortgage Rate Skill Pilot Status

- **Date:** 2026-11-12
- **Version:** v1.0
- **Status:** UAT accepted; pilot remains active
- **Owner:** Luna, HVE CTO / Head Architect
- **Decision authority:** Hans Westphal, CEO
- **Reviewers:** Hans Westphal; Grokbot
- **Scope:** HVE-CFO `best-mortgage-rate` skill and its supervised Spark UAT path

## Executive status

Hans accepted the real-source mortgage-rate skill UAT as a success on
2026-11-12. The pilot is **not closed**. It remains active for continued
hardening, additional supervised use, and measurement of task success, safety,
wall-clock time, human effort, turns/tool calls, and token consumption.

This record marks the mortgage-rate acceptance item complete for the current
pilot phase. It does not represent a production release or unrestricted
financial decision authority.

## Verified outcome

The accepted run used two supplied, unencrypted mortgage PDFs and the bounded
`read_cfo_inbox_text` path. The extraction and skill response completed without
raw/base64 reads, compression warnings, or extraction errors. The structural
run completed within the five-minute performance gate, and HVE-CFO produced a
source-grounded mortgage analysis with page-linked evidence in the Hermes TUI.
The analysis was then written to the controlled CFO Outbox as an HTML report.

The structural evidence record is available on the Spark at:

```text
/srv/hve-outbox/cfo/two-pdf-structural-extraction-uat-report-v1.0.html
```

The successful run established that the active skill can:

- read bounded, page-split PDF text through the intended MCP tool;
- preserve source/page grounding in its analysis;
- separate documented facts from calculations, assumptions, limitations, and
  unanswered questions;
- apply the mortgage-rate calculation boundary correctly; and
- publish a readable HTML deliverable through the controlled Outbox.

No mortgage values are reproduced in this communication.

## Implementation evidence

The HVE-CFO implementation and runtime fixes are published on the `main`
branch:

- [HVE-CFO `5f4af6d`](https://github.com/humanvalueexchange/hve-cfo/commit/5f4af6d)
  — restart active CFO services after deployment.
- [HVE-CFO `a7c850f`](https://github.com/humanvalueexchange/hve-cfo/commit/a7c850f)
  — add timestamped, sortable Inbox/Outbox listings.
- [HVE-CFO `08679c4`](https://github.com/humanvalueexchange/hve-cfo/commit/08679c4)
  — normalize Outbox deliverable versions.
- [HVE-CFO `156223c`](https://github.com/humanvalueexchange/hve-cfo/commit/156223c)
  — make HTML Outbox writes resilient.
- [HVE-CFO `1f52ab2`](https://github.com/humanvalueexchange/hve-cfo/commit/1f52ab2)
  — fix PDF extraction and upload runtime behavior.

## Lessons from the pilot

### 1. Separate Linux-user boundaries are a material operating concern

Running HVE-CFO as `hve-cfo`, with protected home directories and separate
service accounts for the uploader and viewer, introduced real deployment
constraints. A dependency available in the CFO MCP virtual environment was not
available to the system-Python uploader. Pointing a restricted service at the
private CFO virtual environment produced `203/EXEC`; the safer correction was
to make `pypdf` a lazy dependency for PDF extraction while keeping the upload
service on its accessible system interpreter.

### 2. Source, installed, running, and live-rendered states are different

The source repository can contain the fix while the installed adapter is
stale, the service is still running old code, or the live page still renders
old output. The pilot therefore adopts this operational gate:

```text
source diff → focused tests → deploy → explicit service restart
→ live endpoint/tool check → fresh session → UAT
```

`systemctl enable --now` is not sufficient when a service is already active;
the deployment path must explicitly restart active services.

### 3. MCP tool descriptions and schemas must constrain common failure modes

The pilot exposed repeated failures around ambiguous tool selection, stale MCP
tool surfaces, HTML output extensions, and version formats. The adapter now
guards the intended boundaries, but future tools should make valid filenames,
formats, versions, pagination, and prohibited fallbacks explicit in their
schemas and descriptions.

### 4. UAT prompts must preserve scope and test agent autonomy

Prompts that over-specify filenames, introduce unrequested data sources, or
permit open-ended retries can hide the behavior being tested and waste time.
The effective pattern is a narrow task boundary, exact permitted tools,
explicit stop conditions, one bounded write attempt, and no resource browsing
or retry loop after a tool error.

### 5. Live verification is part of completion

A commit or deployment command is not evidence that the runtime is ready.
Completion requires direct confirmation of the live MCP tool list, service
status, endpoint behavior, and rendered artifact. This distinction is now a
required part of HVE-CFO pilot execution.

## Pilot continuation

The mortgage-rate acceptance item is complete, but the pilot continues. Future
work should remain supervised and evidence-led, with no inference that this
skill or HVE-CFO is authorized to make binding lender, filing, payment, or
financial decisions. Additional skill work should use the approved HVE skill
workflow and should record the same efficiency and safety measures.

## Review request

Hans and Grokbot are asked to review this status record, particularly:

1. whether the verified UAT evidence is sufficient to mark the mortgage-rate
   acceptance item complete;
2. whether the Linux-user deployment lessons should become a versioned Spark
   SOP/runbook; and
3. which next supervised pilot capability should be prioritized.

