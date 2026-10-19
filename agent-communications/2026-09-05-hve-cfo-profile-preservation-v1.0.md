# HVE-CFO Profile Preservation Record

**Date:** 2026-09-05  
**Status:** Superseded historical profile draft - not current CFO policy or runtime state  
**Owner:** Hans Westphal  
**Prepared by:** Luna, HVE Head Architect and CTO  
**Profile:** `hve-cfo`  
**Source repository:** `humanvalueexchange/hve-cfo`

> **Superseded historical record:** This document preserves a 2026-09-05
> profile snapshot. Its Bitcoin/trading, drawdown, path, model, and deployment
> statements are not current HVE-CFO instructions. Use the current approved
> profile contracts and live configuration for present-day operation.

## Purpose

This record preserves the current `hve-cfo` Hermes profile and its boundaries
before the profile is built out further. It separates observed runtime state
from approved future architecture. It does not authorize starting the CFO
gateway, changing financial workflows, or enabling any new capability.

## Current profile identity

The current live identity is:

- **Role:** CFO, controller, bookkeeping assistant, and treasury AI for
  HVEGlobal LTD.
- **Primary mandate:** maintain accurate, auditable, filing-ready books while
  protecting treasury value.
- **Reporting line:** Hans Westphal, CEO.
- **Operating surface:** desktop-only.
- **Messaging channels:** no WhatsApp, Telegram, or other messaging gateway.
- **Financial reporting currency:** CAD, while preserving original currencies,
  units, and exchange-rate evidence.
- **Treasury denomination:** SATs for Bitcoin treasury analysis.

The live identity file is maintained outside this repository at:

```text
/home/hans/.hermes/profiles/hve-cfo/SOUL.md
```

The repository must contain the deployable, non-secret copy before any future
profile deployment is approved.

## Current safety boundaries

The preserved profile must continue to:

- avoid placing or authorizing trades;
- require Hans's written approval for consequential treasury actions;
- remain paper-trading-only until Hans authorizes live trading in writing;
- apply the existing 1 percent per-trade, 2 percent daily, and 5 percent
  weekly drawdown limits when analyzing Bitcoin activity;
- preserve source evidence and audit trails for every bookkeeping adjustment;
- separate business and personal transactions;
- flag uncertain tax, mixed-use, shareholder-loan, GST/HST, payroll, and
  foreign-exchange items for review;
- avoid filing returns, remitting tax, making filing elections, or providing
  definitive legal or tax advice without Hans's approval and qualified
  Canadian-accountant review;
- never expose credentials, statements, wallet details, account numbers, or
  other sensitive financial data in Git or operational communications.

## Current runtime snapshot

Observed on 2026-09-05:

| Surface | Current state |
|---|---|
| Profile directory | `/home/hans/.hermes/profiles/hve-cfo` |
| Identity file | Present; CFO identity and desktop-only boundary |
| `profile.yaml` | Not present in the live profile directory at inspection time |
| Model configuration | Live config still declares `qwen3.5:27b-128k` |
| Messaging gateway | No `hve-cfo` gateway is approved or active |
| Dedicated service | `hermes-gateway-hve-cfo.service` is an approved future launch path, not to be started yet |
| Dedicated skills | Intended source: `/home/hans/hermes-cfo/skills/hve`; implementation remains a separate gate |
| Git source | Dedicated `humanvalueexchange/hve-cfo` repository exists |

The live model declaration is stale relative to the approved architecture
record. It must not be silently changed as part of preservation.

## Approved future architecture, not yet implementation

The 2026-09-02 CFO dual-backend decision record approves staged evaluation of:

- primary: `qwen3.8-hermes:27b-128k`;
- deriver: `qwen3.8-distill-2b:q4_k_m`;
- embeddings: `nomic-embed-text`;
- a dedicated native service named
  `hermes-gateway-hve-cfo.service`;
- dedicated workspaces and explicit filesystem allowlists;
- a dedicated CFO skill tree;
- isolation from Hans, librarian, coder, and legacy paths.

Those decisions authorize staged implementation and evaluation only. They do
not claim that the service, model migration, filesystem isolation, or skills
tree has been completed.

## Build-out gates

Before `hve-cfo` is started or connected to any channel:

1. Commit the exact current `SOUL.md`, a sanitized `config` template, and
   `PROFILE.yaml` to `humanvalueexchange/hve-cfo`.
2. Confirm the repository contains no credentials, live databases, session
   files, or statement data.
3. Validate that `hve-cfo` owns no WhatsApp or Telegram route.
4. Implement and review filesystem and workspace allowlists.
5. Implement the dedicated service with a disabled-by-default unit.
6. Validate the approved model stack against live Ollama inventory.
7. Run read-only bookkeeping and reconciliation acceptance tests.
8. Obtain Hans's explicit approval before enabling the service or processing
   consequential financial actions.

## Preservation rule

Until the gates above are complete, treat this document and the live CFO
profile as a preservation baseline. Do not optimize, rename, merge, or
re-purpose the profile from another Hermes repository. Any material change
requires a new versioned communication with owner, rationale, status, date,
and evidence.

## Related records

- `2026-09-02-hve-cfo-dual-backend-decisions-v1.1.md`
- `2026-09-02-hve-cfo-mercury-node-reporting-v1.0.md`
- `2026-08-30-hve-identity-and-authority-index-v1.0.md`
