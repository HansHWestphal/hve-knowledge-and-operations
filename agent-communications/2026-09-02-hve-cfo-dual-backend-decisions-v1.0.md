# HVE-CFO Dual-Backend Architecture Decisions

**Date:** 2026-09-02  
**Status:** Approved decisions and implementation constraints  
**Owner:** Hans Westphal  
**Recorded by:** Luna, HVE Head Architect and CTO  
**Profile:** `hve-cfo`

## Purpose

This document records Hans's decisions following the read-only optimization
assessment of the live `hve-cfo` profile and the outside-in review in
`HVE-CFO-Dual-Backend-Architecture.pdf`.

The PDF remains a proposed architecture reference. This document is the
approved decision record for the CFO profile. Approval authorizes staged
implementation and evaluation; it does not claim that implementation has been
performed or that the profile is production-ready.

## Approved decisions

### 1. CFO primary model

`hve-cfo` will use the local Ollama model:

```text
qwen3.8-hermes:27b-128k
```

This replaces the stale `qwen3.5:27b-128k` declaration in the current profile.
It does not change the `hanshermesagent` model identifier.

The CFO will use the approved three-model Ollama hot stack:

- `qwen3.8-hermes:27b-128k`
- `qwen3.8-distill-2b:q4_k_m`
- `nomic-embed-text`

No fourth hot LLM is approved. `gpt-oss:120b`, generic `qwen3.8:27b`, and
other superseded large-model alternatives are excluded from this architecture.

### 2. CFO launch path

The approved launch path is a dedicated native systemd user service:

```text
hermes-gateway-hve-cfo.service
```

The service will launch Hermes with the `hve-cfo` profile and remain isolated
from the `hanshermesagent`, `hve-librarian`, paused `hve-coder`, and legacy
`hermes-coder` paths.

The service must not be enabled or started until the profile safety controls
and implementation gates are reviewed.

### 3. Workspace and filesystem isolation

`hve-cfo` will use a dedicated workspace and explicit filesystem allowlists.
The approved CFO writable scope is limited to dedicated books, receipts,
tax-corpus, and treasury-report areas.

The CFO must not write to:

- the coder workspace;
- shared project roots;
- other profiles' homes, sessions, memories, or databases;
- credentials, authentication files, or environment-secret files.

A `terminal.cwd` setting alone is not sufficient isolation.

### 4. Dedicated skill source

The approved skill source is a dedicated CFO tree:

```text
/home/hans/hermes-cfo/skills/hve
```

It will contain only approved bookkeeping, reconciliation, tax-evidence,
treasury-analysis, RAG, and reporting workflows. The CFO must not implicitly
load another profile's skill tree.

### 5. Deterministic finance layer

The model may classify, extract, draft, explain, and cite. Deterministic tools
must own:

- CSV parsing;
- allocation percentages;
- reconciliation totals;
- GST/HST and other tax calculations;
- balances and report totals;
- other numeric financial outputs.

Ledger changes must be append-only and require a human or an explicitly
approved deterministic ledger engine. The model must not invent or
independently post journal entries, tax payable, rates, or balances.

### 6. Tax-corpus scope

The approved local corpus uses Canada/Ontario materials as the default and
United States IRS materials only as an explicit overlay for US-side questions.
Retrieved rules must be cited to source passages and treated as research,
not as definitive legal or tax advice.

The architecture scope records the proposed Ontario CCPC and dual
US-Canadian-family context as the approved working frame for corpus design.
This does not authorize a filing position, tax treatment, tax amount, or legal
conclusion. Final tax authority remains with Hans and a qualified Canadian
accountant where applicable.

### 7. CFO MCP and tool permissions

The CFO will use a dedicated MCP/tool allowlist centered on:

- `cfo-ledger`;
- `cfo-rag`;
- `cfo-receipts`;
- `cfo-reports`.

These tools must be local, provenance-aware, and read-only or append-only.
The CFO surface must not include:

- GitHub issue creation, voting, or commenting;
- messaging channels;
- trade execution;
- filing submission;
- payments or transfers;
- cross-profile writable access.

The current general-purpose HVE MCP exposure is not the approved final CFO
tool surface.

### 8. Fallback and cloud boundary

`hve-cfo` will operate fail-closed with no automatic cloud fallback by default.
Bank CSVs, statements, receipts, tax slips, SINs, account numbers, wallet
data, and private books must never leave the DGX Spark.

Any future fallback requires a separate approved decision defining the provider,
sanitization rules, egress boundary, user-visible indication, and rollback
behavior.

### 9. Financial-data retention and memory

Financial source documents are evidence artifacts, not general profile memory.
The implementation must:

- enable appropriate PII protection;
- minimize or disable persistent prompt storage where operationally safe;
- require approval for financial-memory writes;
- avoid copying raw statements, receipts, tax slips, credentials, or account
  numbers into general memory;
- retain only necessary provenance such as source ID, period, hash, timestamp,
  classification status, and evidence references.

### 10. Promotion and rollback gate

`hve-cfo` must remain staged and must not replace the prior CFO operating path
until the following evidence is recorded:

1. Held-out mixed-use classification benchmark, including precision for
   mixed-use and benefit-risk labels.
2. Human-scored receipt extraction for vendor, tax, amount, purpose, and
   mixed-use handling.
3. Cited CRA/Ontario and explicitly approved US-overlay RAG tests.
4. Zero invented tax-payable results on a calculation-trap test set.
5. Cold and warm p50/p95 latency results.
6. Twenty-minute mixed-load memory stability results.
7. Workspace and MCP isolation validation.
8. Tested rollback to the prior CFO path and model tags.

Promotion does not authorize filing, payment, trade, or other irreversible
actions. Hans remains final authority.

## Explicit non-goals

- No HVE-Coder profile, vLLM service, Nemotron deployment, or coder retirement
  work is authorized by this record.
- No `hermes-coder` retirement is authorized.
- No fourth hot LLM is authorized.
- No CFO trade execution is authorized.
- No tax filing, remittance, filing election, or definitive tax/legal advice is
  authorized.
- No cloud fallback for raw financial data is authorized.

## Implementation gates still open

Before implementation, the following technical details require a separate
review against the approved decisions:

- exact systemd unit and environment wiring;
- exact workspace and filesystem allowlists;
- dedicated skill inventory and loading validation;
- CFO MCP server implementation and append-only semantics;
- local tax-corpus provenance and update process;
- deterministic calculator and ledger-engine design;
- bounded max-turn, retry, timeout, and reasoning settings;
- prompt-retention and PII-redaction behavior;
- synthetic or approved test evidence;
- observability and rollback procedure.

No profile or runtime change has been made by this record.

## Evidence

- `instructions.md`
- `AGENTS.md`
- `2026-08-29-hve-operating-plan-v1.1.md`
- `2026-08-30-hve-identity-and-authority-index-v1.0.md`
- `2026-08-30-hve-hermes-memory-authority-v1.0.md`
- `2026-09-02-hve-coder-dual-backend-decisions-v1.0.md`
- `HVE-CFO-Dual-Backend-Architecture.pdf`
- Live read-only review of `/home/hans/.hermes/profiles/hve-cfo/`
- Live read-only systemd, Ollama, MCP, and Open WebUI health evidence on
  2026-09-02
