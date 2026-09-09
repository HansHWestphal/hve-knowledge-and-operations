# HVE-CFO and Mercury Node Reporting and Operations

**Date:** 2026-09-02  
**Status:** Approved reporting and operational constraints  
**Owner:** Hans Westphal  
**Recorded by:** Luna, HVE Head Architect and CTO  
**Scope:** Future HVE-CFO integration with `humanvalueexchange/mercury-node`

## Purpose

This document records Hans's decisions defining the future relationship between
HVE-CFO and Mercury Node. It supplements the approved CFO architecture record
and does not authorize profile, service, credential, API, or runtime changes.

The `humanvalueexchange/mercury-node` repository remains an independently
maintained Bitcoin and Lightning node operator system. Its current public
documentation describes a Raspberry Pi-class ARM64 deployment with Bitcoin
Core, LND, BTCPay Server, NBXplorer, a local operator CLI, and a local agent
API. Its registry and complete command authorization migration are not yet
complete.

## Authority model

```text
Hans / CEO and final authority
        |
     HVE-CFO
        |
   Mercury Node
```

This model means:

- Hans retains final authority over treasury, payments, transfers, tax, legal,
  and irreversible company decisions.
- HVE-CFO owns financial control, treasury analysis, reconciliation, approval
  packages, and financial reporting.
- Mercury Node is HVE-CFO's operational Bitcoin/Lightning direct report.
- Mercury owns node operations and may prepare or perform only explicitly
  approved operational actions.

The reporting relationship does not grant HVE-CFO unilateral execution
authority or override Mercury's own operational safety controls.

## Approved decisions

### 1. Bitcoin/Lightning reporting relationship

HVE-CFO may direct Mercury Node for approved financial-control and operational
reporting work. Mercury owns Bitcoin Core and LND operations, node telemetry,
Lightning state, operational preparation, and controlled execution.

HVE-CFO remains the financial analyst/controller and does not become a wallet
custodian or unrestricted node operator.

### 2. CFO-to-Mercury command scope

The default CFO interface is read-only and prepare-only. HVE-CFO may request:

- node and service telemetry;
- reconciliation-data collection;
- evidence packaging;
- health and synchronization checks;
- preparation of operational plans.

HVE-CFO may not directly invoke:

- fund movement;
- channel changes;
- fee changes;
- rebalancing;
- purchases;
- other node-state mutations.

### 3. Human approval for execution

Every fund-moving or node-state-changing Mercury operation requires explicit
human confirmation through Mercury's approved execution boundary, including:

- Lightning payments;
- on-chain sends;
- channel open or close;
- rebalancing;
- fee changes;
- purchases.

HVE-CFO and Mercury must never self-approve one another.

### 4. Authenticated local integration

Future integration will use a dedicated local CFO-to-Mercury adapter with:

- authenticated typed read, prepare, and execute operations;
- localhost binding;
- short-lived preparation tokens;
- plan expiry;
- idempotency protection;
- audit receipts.

HVE-CFO must not receive wallet seeds, LND macaroon material, withdrawal
credentials, unrestricted shell access, or unrestricted raw Mercury API access.

No public MCP, public registry, or unauthenticated remote control surface is
approved by this record.

### 5. Mercury read-data scope

HVE-CFO may receive Mercury evidence for:

- node health;
- chain and Lightning synchronization;
- wallet and channel balances;
- invoices;
- payment history;
- routing fees;
- on-chain transaction history;
- channel state;
- backup status;
- relevant operational logs.

Data must be limited to what is needed for treasury reporting and
reconciliation. Secrets, wallet seeds, macaroon contents, and unrelated
personal data remain excluded.

### 6. Prepared-operation contract

Every future Mercury prepared operation must include:

- plan ID;
- requested action;
- amount and unit;
- destination or channel scope;
- fee estimate;
- risk flags;
- source evidence;
- required approver;
- expiry;
- idempotency key.

Prepared plans must never broadcast or mutate state. Execution must produce an
immutable receipt or an explicit rejection, with the plan and approval
identifiers linked.

### 7. Reporting cadence and escalation

The approved future reporting rhythm is:

- daily operational and treasury summaries;
- weekly reconciliation and control review;
- immediate escalation for chain or Lightning desynchronization;
- immediate escalation for backup failure;
- immediate escalation for liquidity or custody risk;
- immediate escalation for unexpected fund movement;
- immediate escalation for permission changes;
- immediate escalation for rejected or expired execution plans.

Reports must cite source timestamps and clearly distinguish raw telemetry from
HVE-CFO analysis.

No cron job or notification channel is created by this record.

### 8. CFO-Mercury promotion gate

The integration must remain staged until it passes:

- read-data correctness;
- reconciliation accuracy;
- permission and secret isolation;
- prepare-without-broadcast tests;
- explicit-confirmation enforcement;
- idempotency and expiry tests;
- receipt and audit tests;
- degraded-service behavior;
- rollback to the prior independent Mercury and CFO paths.

No production integration, service change, or execution capability is
authorized by this gate alone.

## Explicit non-goals

- No direct HVE-CFO trade execution.
- No direct HVE-CFO withdrawal or transfer authority.
- No automatic Mercury payment or channel execution.
- No wallet-seed, macaroon, or private-key exposure to HVE-CFO.
- No unrestricted CFO shell access to the Mercury host.
- No public MCP or unauthenticated Mercury control endpoint.
- No changes to the Mercury Node repository or deployment.
- No changes to the paused HVE-Coder, vLLM, Nemotron, or `hermes-coder` paths.
- No live service, cron, notification, or credential changes by this record.

## Implementation gates still open

Before implementation, the following require a separate technical review:

- exact adapter protocol and authentication mechanism;
- exact read and prepare schemas;
- execution confirmation handoff;
- plan-signing, expiry, and idempotency implementation;
- receipt format and retention;
- Mercury API and CLI registry completion requirements;
- data minimization and account-scope rules;
- reporting transport and delivery channel;
- synthetic test fixtures and held-out reconciliation data;
- observability and rollback procedure.

## Evidence

- Public `humanvalueexchange/mercury-node` repository:
  `https://github.com/humanvalueexchange/mercury-node`
- Mercury `README.md`, `docs/architecture.md`, `docs/current-state.md`, and
  `SECURITY.md`, read on 2026-09-02
- `2026-09-02-hve-cfo-dual-backend-decisions-v1.1.md`
- `2026-09-02-hve-coder-dual-backend-decisions-v1.0.md`
- Hans's eight official decisions recorded during the 2026-09-02 CFO-Mercury
  reporting and operations review

No profile, service, credential, API, or runtime change has been made by this
record.
