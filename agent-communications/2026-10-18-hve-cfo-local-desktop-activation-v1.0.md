# HVE-CFO Local Desktop Activation Under Risk Override

- **Date:** 2026-10-18
- **Status:** Approved for local Hermes Desktop use; release controls remain open
- **Decision owner:** Hans Westphal, CEO
- **Recorded by:** Luna, HVE Head Architect and CTO
- **Profile:** `hve-cfo`

## Decision

Hans authorized HVE-CFO for local Hermes Desktop use with real financial
records. He declined a synthetic-data test and explicitly accepted the
unverified controls listed below. This is a scoped activation decision, not
evidence that those controls passed or that HVE-CFO is production-release
validated.

## Scope and boundaries

- Local Hermes Desktop and local Ollama inference only; private financial
  information must not be sent to cloud providers or public sites.
- Personal and HVE Business data require explicit context selection. Cross-
  domain analysis still requires an explicit request.
- Local finance tools are limited to CSV aggregation and exact-key,
  report-only reconciliation. Document operations must preserve source files
  and write only new or edited copies under the selected CFO output directory.
- No trades, payments, transfers, withdrawals, filings, ledger postings, or
  final treasury decisions.
- External channels and HVE-Coder-Jr dispatch remain disabled.

## Runtime evidence

At 20:18 EDT, the Hermes Desktop supervisor had started a fresh `hve-cfo`
backend after the live config edit. The local finance and document MCP server
processes were running and the Desktop connection had re-established. The
configured primary and auxiliary Ollama models were resident on GPU with their
target contexts. No CFO conversation, financial file, or inference request
was processed by Luna during this activation.

## Accepted but unverified controls

- Full Hermes template conformance remains open; the source template is schema
  v23 and the live profile config is schema v39.
- Effective Desktop tool discovery, per-tool permissions, data-root isolation,
  output-copy behavior, and rollback remain unverified.
- Normal Hermes sessions may retain conversation content and tool arguments.
  In the live config, session auto-pruning is disabled and the configured
  retention threshold is 90 days; records may therefore remain indefinitely.
  This is separate from the curated-memory plugin, which excludes raw turns.
- The profile's SQLite memory initialization and retrieval remain unverified.

These gaps are recorded as accepted risks for current local use, not as passed
release gates. No synthetic data was used.

## Evidence and provenance

- Hans's explicit approval in the 2026-10-18 session, including selection of
  the option to override the gates and accept the listed risks.
- Local HVE-CFO source evidence in `humanvalueexchange/hve-cfo`, including
  `RELEASE.yaml` and `evidence/agent-card-evidence.yaml`.
- Live process, MCP child-process, config timestamp, and Ollama model-residency
  observations made at 20:18 EDT on 2026-10-18.
