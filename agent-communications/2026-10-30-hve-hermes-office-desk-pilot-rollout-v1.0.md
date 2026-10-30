# Office Desk (Hermes plugin) — Reference & Fleet Pilot Rollout

**Tag:** Discussion Draft · Decision‑Input. **Not an install action. Not HVE policy. No profile is modified by this document.**
**Source:** @HermesWatcher — **unofficial** X account (self‑describes as *Unofficial. Not affiliated with Nous Research*). status `2115972001026425256`, posted **1:00 AM, Oct 30, 2026**, 10K views.
**Indexed in HVE knowledge library:** `doc 2c1087560980cc27` · 2 chunks · **content verified** (HTTP 200, full post text retrieved — not a login shell).
**Repo referenced in the page:** `DECRUX9812/hermes-office` (**community slug**, not `NousResearch/…`). The claim that it is "in the Hermes plugin catalog" is **the post's, not independently verified**.
**Compiled by:** HVE‑Librarian (2026‑10‑30).
**Decision owner:** Hans (CEO). **Execution owner (if approved):** Luna (Technical Architect).

---

## What the post claims it does (fact, as posted — not endorsement)
- **Word** edits return as **tracked changes + comments** (redline‑style).
- **Excel** edits get **formulas recalculated**, so totals stay right.
- **PowerPoint** slides edited **in place**.
- Review everything on the **"Desk" page in Hermes Desktop**, **accept with one click**.
- Every change gets a **backup + an undo receipt**.
- **Scoped to the "folders you put on the Desk."**
- **Default posture:** *"Nothing changes until you say OK."* — approval‑gate + receipts + scope, by design.
- Use cases named: change contract terms and see what moved; add a budget line without touching a formula; sync a pitch deck's price/terms; one request across all three files.

## HVE lens (interpretation — not a recommendation)
- **Approval‑gate + revert‑receipt + folder‑scope** aligns with HVE's preserve‑and‑route posture: originals preserved, decision routed to Hans (authority), reversible by default.
- **Provenance risk:** community repo + unofficial source + unverified "official catalog" claim. Treat as a **candidate to verify and evaluate**, not a catalog fact.
- **Domain note:** this is an **office‑file editor with approval gates**, a **different domain** from the 24‑memory‑plugin doc. Kept as a **companion**, not folded into `2026-10-29-hve-hermes-fleet-memory-options-v1.0.md`.

## Pilot rollout — Hans's stated direction (recorded, attributed to Hans)
- **Decision (owner: Hans, CEO):** Office Desk will be rolled out to the **whole HVE fleet eventually** once it proves out. **Pilot set first:** `hve-librarian`, `hve-chief-of-staff`, `hve-cfo` (Hans's words: *"we will start with hve-librarian, hve-chief of Staff and hve-cfo"* — canonical slug `hve-chief-of-staff`).
- **Execution (owner: Luna, Technical Architect):** verify, install, and configure the plugin on the pilot profiles; owns infra + privacy for the rollout. **Not yet executed; execution plan pending.**
- **Status:** Decision stated (Hans). Evaluation + scoped rollout **pending** (Luna).

### Open items for Luna / Hans before install (do not carry forward as fact)
- **Repo check:** confirm `DECRUX9812/hermes-office` is the correct, canonical, and maintained repo (vs. a fork or name‑square).
- **Egress / residency:** local‑only vs. network model; does it store anything off‑host?
- **Per‑profile scoping + sandboxing:** each profile's "Desk" folders isolated so one profile's files are not reachable by another.
- **Coexistence:** must not clobber originals; must play with the profiles' current docx/xlsx/pdf tooling (HVE never modifies originals).
- **Backup / undo semantics:** who can revert, and role/authority mapping — especially `hve-cfo` (financial docs) and `hve-chief-of-staff` (coordination docs).
- **Approval authority:** the "say OK" approver must map to **Hans / named approver**, not the agent itself.

## Provenance & disclaimers
- Source is an **unofficial** X account; community repo slug; third‑party "catalog" claim **not verified**.
- Post date **Oct 30, 2026**; captured `2026-10-30T19:03Z`; full text + repo slug preserved in the HVE knowledge library (`doc 2c1087560980cc27`).
- This document **records Hans's stated pilot direction and the decision frame**; it does **not** install, endorse, or modify any profile. **No fleet changes are made by this file.**
- The pilot rollout is a **decision‑input awaiting Luna's evaluation and Hans's go**; it is not a commitment and does not create an external obligation.
