# Elephant-Goldfish Workflow — HVE Adaptation (Luna × Coder Jr)

**Status:** APPROVED by Hans (Hans Westphal, Telegram, 2026-10-31). Operationalization routed to Hermes (kanban t_95122e88); committed to repo as system of record.
**Date:** 2026-10-31 · **Drafted by:** HVE-Librarian, from Hans's Telegram direction · **Approved by:** Hans Westphal
**Owner for approval:** Hans Westphal (CEO, final authority)

## Source provenance

- X post: @thisguyknowsai, 31 Oct 2026 — `https://x.com/thisguyknowsai/status/2116453452977152209` (retrieved 31 Oct 2026)
- Repo: `https://github.com/google/elephant-goldfish-model` — Apache-2.0, ~7,035 stars, created 2026-09-13 (verified via GitHub API 31 Oct 2026)
- README headline claim "thousands of Google engineers use EGM" is **the repo's own marketing text**, not independently verified.
- Source link filed in the HVE knowledge library (hve-link-collector, 2026-10-31).

## 1. The model (as stated in the post and repo README)

- **Elephant** — one long-context, long-running session that holds the architecture, intent, and every decision. Writes zero code. Interviews and argues with the human; keeps the record.
- **Goldfish** — fresh, zero-context sessions. Implement and review without the earlier conversation, so they don't inherit its blind spots.
- **You (human)** — make the architectural trade-offs and approve the specification before implementation.
- **Pipeline:**
  1. `egm-brainstorm` — Elephant and human debate options under a strict no-code rule.
  2. `egm-draft` — Markdown design doc: problem, plan, alternatives, exact files to change.
  3. `egm-review` — one Goldfish must explain the design back; if wrong, the doc is ambiguous and goes back for redraft.
  4. Hostile Goldfish reviewers — hunt edge cases, hidden dependencies, logic gaps.
  5. Final Goldfish go/no-go — file paths, data structures, function signatures all present and unambiguous.
- **Scope:** features that need design decisions before implementation. Small, clear bug fix → normal coding workflow (per README).
- **Install targets (README):** Antigravity CLI/App/IDE, Claude Code, Codex, Claude Cowork, ChatGPT Work. Post notes: Antigravity-first, other environments coming; security is **not** on the default reviewer list.

## 2. HVE mapping (proposal)

| EGM role | HVE role | Notes |
|---|---|---|
| Elephant | **Luna** (Technical Architect) | Long-running context over HVE Life OS architecture and intent; interviews Hans; drafts the design doc. Strict no-code rule: proposes, never implements. |
| Goldfish (implementer) | **Coder Jr** | Fresh session; builds only from the design doc + referenced sources. No architecture calls. |
| Goldfish (hostile reviewer) | Coder Jr in a separate fresh session | Reviews without the implementation context; reviewer persona per EGM rules. |
| Goldfish (go/no-go) | Coder Jr, final fresh session | Unambiguity checklist: files, data structures, signatures. Fail → back to Luna, not improvised. |
| Human approver | **Hans** | Architectural trade-offs and spec approval sit with him (SOUL authority order). |

## 3. Operating rules (if adopted)

1. No code before the design survives review; the no-code rule binds the Elephant.
2. No self-grading: the reviewing Goldfish is never the implementing Goldfish.
3. Context isolation: Goldfish sessions receive the design doc and repo only — never the design conversation.
4. Ambiguity is a defect: a failed read-back goes back to the Elephant, not into improvisation.
5. HVE adds its own **security Goldfish** pass (not in EGM defaults) for anything touching credentials, financial, or private data — HVE boundary constraint.
6. Small, clear bug fixes: skip EGM and use the existing coding SOP (`SOPs/2026-09-11-hve-spark-coding-task-sop-v1.2.md`).

## 4. Open questions (for Hans)

1. **Where the workflow lives:** (a) install the EGM plugin on the coding harnesses on the Spark (Antigravity / Claude Code / Codex), (b) port the rules and reviewer personas into HVE skills for Luna/Coder Jr (Hermes/Luna lane, not librarian), or (c) keep it as a process memo and run it ad hoc.
2. **Public content:** do we ship an HVE-branded post? Draft in §5.
3. **Approval to commit** this document to the repo (system of record). — *Resolved 2026-10-31: approved by Hans; committed and pushed.*

## 5. Draft HVE X post (Hans voice, for approval — not published)

> Google open-sourced their coding workflow: Elephant-Goldfish.
> One deep-memory agent designs. Writes zero code.
> A fresh batch of amnesic agents attack the design until it survives.
> Stealing it for HVE. Luna's the elephant. Coder Jr's the goldfish.
> Design first. Then build.
