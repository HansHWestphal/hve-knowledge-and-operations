# HVE Team Tasking & Delivery Workflow — Requirements & Decisions

**Prepared by:** Hermes (Chief of Staff), HVE
**Date:** 2026-09-05
**Status:** FINALIZED (requirements + decisions) — awaiting Luna's technical review
**Requested review:** Luna (CTO / technical architecture) — opinion + improvements before build
**Approved by:** Hans Westphal (CEO) — all decisions below confirmed in DM, 2026-09-04/05
**Purpose:** Single record of the complete discussion and key decisions on how the HVE
team (Alan, Brian, Wolfgang) will receive, execute, and deliver tasks. Nothing in this
document is built yet. Build starts after Luna's review.

---

## 1. Background

HVE is advancing across the Five Wealth pillars and needs to assign and track
tasks across three human team members:

- **Alan** — physical/fitness (nutrition plans; first task: updated bio for hve-website)
- **Brian** — financial/insurance (IUL research lane, Financial Wealth pillar)
- **Wolfgang** — time/social (Time Wealth support, Instagram, content)

Prior state: no formal tasking for any of the three existed in the decision
ledger or in the repo (verified 2026-09-04 across `agent-communications/` and
the HVE decision ledger; zero assigned-task items). This document is the
requirements record for the new tasking system.

## 2. Core design principles (agreed with Hans)

1. **Hans's time and the team's time are precious** — optimize human time spent;
   least possible friction for team members.
2. **Hans retains final authority** — no task is closed without his validation.
3. **GitHub = system of record** provenance, auditable history, no email scatter.
4. **DM (Hans ↔ Hermes) = decision space.** Team group chat = communication
   space. No external commitments without Hans.
5. **Hermes is the project manager** for the three humans; Kanban/agent-board
   tooling is the wrong layer for human-owned work (it routes to Hermes
   profiles, not people).

## 3. Decided items

### D1 — Tracking surface: GitHub Projects (new dedicated repo + project)
- New repo: **`humanvalueexchange/hve-team`** (public at launch; see D3).
- Separate from `hve-knowledge-and-operations` (ops/financials, stays as-is)
  and from `humanvalueexchange/humanvalueexchange` (private; its existing
  project "HVE Life OS — Logical Architecture Roadmap" is software dev
  tracking and NOT reused for team delivery).
- One **GitHub Project** board: **"HVE Team Delivery"**, columns:
  `Open → In Progress → Awaiting Validation → Done`.
- Card fields: **Owner** (prefilled by Hermes at card creation — team members
  never type it), **Due** (optional), **Pillar**
  (Time / Physical / Mental / Social / Financial).
- Card body always contains the full deliverable spec, so opening a card is
  one-read complete.
- `README.md` = the "one link" reference page: board link + "how to complete a
  task in 20 seconds" (group-chat flow).
- Folder for work artifacts: **`uploads/alan/`, `uploads/brian/`,
  `uploads/wolfgang/`** — all deliverables live in this one repo (decision:
  everything in one place).

### D2 — Friction model: WhatsApp group is the team's working surface
- Team members do **all** task work via the HVE team group:
  - Ask "what are my tasks?" → Hermes replies with their open cards.
  - Report status ("starting", "blocked") → Hermes moves the card, logs the
    reason, DMs Hans the flag.
  - Deliver a digital artifact → paste/drop it in the group → **Hermes commits
    it to `uploads/{name}/` on their behalf** and links it to the card. They
    never need the repo to do that.
  - Report a physical/real-world task done → one message → card to
    Awaiting Validation.
- **Zero-GitHub-account path works for the entire Phase 1** (public repo +
  no-login viewing + Hermes-committed artifacts).
- The GitHub board is Hans's PM surface and an *optional* self-serve window
  for the team (link works without login while public).
- Onboarding follow-up (soft, not a gate): each member gets a task to create
  a GitHub account and make one real commit, ahead of the flip to private.

### D3 — Visibility: Phase 1 public → Phase 3 private
- **Phase 1 — Onboard:** public `hve-team`; only low-sensitivity,
  public-facing content (bios, website copy, public task summaries).
  Sensitive work (Brian's IUL/financial, health/nutrition detail, strategy)
  stays in DM + decision ledger until the flip.
- **Phase 2 — Accounts:** team members create GitHub accounts; first
  self-commits.
- **Phase 3 — Full:** repo goes private (one command; content + history
  identical, only the lock turns on). All Five Wealth work + sensitive
  artifacts live here; team commits directly; Hans validates.

### D4 — Validation gate (Hans only)
- Team reports "done" → status becomes **`Awaiting Validation`** (never
  auto-closes).
- Hermes DMs Hans a ping per pending validation (batch-capable).
- Hans approves → `Done` (with date + evidence). Hans rejects → card reverts
  to open state with reason recorded.
- **Nothing is formally closed without Hans's explicit sign-off.**

### D5 — Scope gate (Hans only)
- New tasks / scope changes: must be confirmed by Hans in DM **before** the
  card is created and **before** anything is communicated to the group.
- Hermes drafts the group message in the DM first; approval required before
  broadcast. No half-agreed tasks reach the team.
- Status updates / completion reports on existing cards are logged directly
  by Hermes (tracking, not commitment).

### D6 — Channel topology (verified live, 2026-09-05)
- **DM (Hans ↔ Hermes):** decision, correction, approval, validation space.
- **HVE team group:**
  - WhatsApp group ID: `120363428227646086@g.us`
  - Renamed by Hans to match the mission (2026-09-05; new name: see group
    metadata — renamed from "Hans Westphal Digital Twin Intro").
  - Hermes is a member; responds on @mention (`require_mention: true`,
    `group_policy: open`).
  - **Test passed:** connection check sent to the group, Hermes responded in
    the group and confirmed the channel is wired.
- Hermes cannot enumerate its own groups from the DM; it records the chat ID
  from arriving messages. Group ID above is confirmed via channel directory.

## 4. Full lifecycle (final)

```
Hans DM: assign/confirm task
    → Hermes normalizes, Hans approves
    → card created (Open; Owner/Due/Pillar set by Hermes)
    → group message drafted in DM → Hans approves → broadcast to team

Team (group chat): "starting BT-02"
    → Hermes moves card to In Progress (logged, no approval needed)

Team (group chat): artifact or "done"
    → Hermes commits artifact to uploads/{name}/, card → Awaiting Validation
    → Hermes DM ping to Hans

Hans DM: "done" (or "no — [reason]")
    → Done (date + evidence recorded)  /  card reverts, reason logged

Hermes ongoing: stale-item chasing, weekly "who-owes-what" digest to Hans
```

## 5. First task (validated by Hans)

- **AL-01 — Alan's updated bio for hve-website.**
  Alan delivers it in the HVE team group → Hermes commits to
  `uploads/alan/` → Awaiting Validation → Hans validates → Done → bio pulled
  into the website repo/CMS (separate step).

## 6. Boundaries / guardrails

- No sensitive deliverables (financial, health, tax, strategy) enter the
  public repo during Phase 1 — period.
- No external commitments by Hermes in any channel.
- Group name is final after rename; team told not to change it.
- Board content = approved tasking only; drafts and unapproved policy never
  land in the repo.

## 7. Open items / next steps

1. **Luna review (this doc):** confirm the Projects-board schema works in
   org practice; suggest any field/column improvements; flag any GitHub
   permissions, visibility-flip, or collaboration pitfalls (e.g.,
   `uploads/` as the artifact channel vs. GitHub Releases/PRs; commit
   attribution when Hermes commits on a team member's behalf).
2. After Luna sign-off + Hans's go: create `humanvalueexchange/hve-team`,
   the Project board, `uploads/` folders, README.
3. Post the corrected "board is at hve-team" note to the HVE team group
   (supersedes the earlier confirmation that referenced the old path).
4. Create AL-01 (Alan's bio) as the first card and broadcast to the group.

---

### Appendix A — Decision log (condensed)

| # | Decision | Owner | Date |
|---|----------|-------|------|
| D1 | GitHub Projects in new `hve-team` repo (public at launch) | Hans | 2026-09-05 |
| D2 | Team works 100% via WhatsApp group; Hermes commits on their behalf | Hans | 2026-09-05 |
| D3 | Public → private is a phased flip, not a rebuild | Hans | 2026-09-05 |
| D4 | Awaiting Validation gate; only Hans closes tasks | Hans | 2026-09-04 |
| D5 | DM-first approval before any group broadcast | Hans | 2026-09-04 |
| D6 | HVE team group (`...8627572`-referenced; ID `120363428227646086@g.us`) is the team channel | Hans | 2026-09-05 |
