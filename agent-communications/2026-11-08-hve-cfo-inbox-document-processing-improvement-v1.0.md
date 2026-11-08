# HVE-CFO Inbox Document Processing Improvement — Prompt for Luna

- **Date:** 2026-11-08
- **Status:** Draft for CEO review before Luna tasking
- **Decision owner:** Hans Westphal, CEO
- **Intended recipient:** Luna, HVE Head Architect and CTO
- **Profile:** `hve-cfo`
- **Related:** hve-cfo local desktop activation (2026-10-18); Equifax credit report digest failure (2026-11-08)

## Purpose

Provide Luna with a clear tasking prompt to improve the cfo-inbox document processing path so that hve-cfo can reliably digest PDFs (and similar documents) from the approved inbox channel without multi-minute stalls, consent-gate timeouts, or wasted turns.

This note is based on the After Action Report from the failed attempt to digest `efx-creditreport_20261108-v1.0.pdf`.

## Background (from hve-cfo AAR)

Task: Digest Equifax credit report PDF from CFO inbox and deliver a summary.  
Window: ~15 minutes across 7 turns against a ~2-minute expected bar.  
Status: Not delivered. File confirmed present; full content retrieved via `read_cfo_inbox` (returned base64, persisted to spillover); extraction step (decode + `pdftotext`) hit a 60-second consent gate that timed out. Report content was never read.

### Ranked root causes (AAR)
1. Carried a stale tool-surface belief from a previous task instead of probing the live MCP surface once.
2. Ignored the already-loaded `hve/pdf` skill that named the correct tool.
3. Multiple blocked or zero-information probes (search_files, terminal ls of managed paths, bad Python checks).
4. Critical path forced through a human consent gate for a non-destructive local extraction step (base64 decode + pdftotext on a scratch file).
5. Context bloat (prior-task compaction + 50 KB spillover preview) multiplied the cost of every wasted turn.

### Ideal path that should have worked (~5 calls, 2–3 minutes)
1. Load/confirm `hve/pdf` skill.
2. Optional: `read_cfo_inbox` list to verify filename/size.
3. `read_cfo_inbox` read → content retrieved and persisted.
4. One terminal step: decode base64 to scratch + `pdftotext -layout`.
5. Read extracted text and deliver page-cited summary.

## Prompt for Luna

**Task:** Improve the cfo-inbox document processing capability for the `hve-cfo` profile so that PDF (and similar document) digests complete reliably and quickly under local-only constraints.

**Context:** On 2026-11-08, hve-cfo failed to digest an Equifax credit report PDF after ~15 minutes. The AAR identifies a combination of agent-side process errors and environment/interface friction. The strongest single infrastructure fix is to remove the base64 → terminal decode → consent gate detour from the critical path.

**Required improvements (priority order):**

1. **Add a text extraction tool on the inbox server (highest priority).**  
   Implement something like `read_cfo_inbox_text` (or equivalent) that performs server-side text extraction and returns page-split text with offset/limit pagination. This eliminates the large base64 blob, spillover file detour, terminal decode step, and mid-path consent gate. The entire digest remains inside the trusted, already-approved server boundary.

2. **Reduce tool-surface skew.**  
   The session prompt’s function list was stale relative to the live MCP registry. Investigate and fix so that when MCP tools become available (or change), the agent either sees an updated function list or has a cheap live inventory/probe mechanism. Document the expected behavior.

3. **Narrow allowlist for non-destructive extraction steps (if text tool cannot fully replace them).**  
   Consider auto-approving a tightly scoped set of ephemeral, local, profile-home operations required for document extraction (`pdftotext`, `pdfinfo`, base64 decode to scratch, scratch writes). Do not broaden general terminal or file-system permissions. Prefer removing the need for these steps over lengthening timeouts.

4. **Update the `hve/pdf` skill.**  
   Document that `read_cfo_inbox` currently returns base64 (not text), the decode/extract recipe, and that extraction may currently be consent-gated. Add an explicit probe rule: if a skill names a tool that is not in the known function list, probe it once rather than carrying “tool unavailable” conclusions across tasks. Encode the preferred path once the new text tool exists.

5. **Session hygiene guidance.**  
   Add a short note (skill or memory) that failed-task conclusions should not be automatically imported into the next unrelated task without a live probe.

**Constraints (must preserve):**
- Local Hermes Desktop + local Ollama only; no cloud transmission of financial documents.
- Personal vs HVE Business data isolation remains explicit.
- No autonomous external actions, payments, filings, or ledger writes.
- “Silence is not consent” remains the correct default for any remaining gated steps; prefer path redesign over timeout extensions or bypasses.
- Changes must be compatible with the existing 2026-10-18 local-desktop activation decision and current risk acceptance.

**Deliverables expected from Luna:**
- Implementation plan or direct changes for the inbox server text tool (or equivalent).
- Updated `hve/pdf` skill text.
- Brief note on how tool-surface freshness will be handled going forward.
- Confirmation that the Equifax PDF (currently persisted at `/home/hve-cfo/.hermes/cache/spillover/call_5ipa9emi.txt`) can be processed end-to-end under the improved path once changes land.

**Success criteria:**
- A PDF digest from the CFO inbox completes in a small number of turns (target < 3–4 minutes on the local model) without mid-path consent timeouts.
- No large base64 blobs in the agent context for routine digests.
- Skill and live tool surface stay aligned.

## Current state (as of AAR)

The full PDF content is already persisted at `/home/hve-cfo/.hermes/cache/spillover/call_5ipa9emi.txt` via the approved channel. It has not been read. One approved extraction step remains if the current path is used; the preferred outcome is that future documents never require that step.

## Evidence

- hve-cfo After Action Report, 2026-11-08 (Equifax PDF digest failure).
- Existing hve-cfo local activation decision (2026-10-18).

---

*This note is staged for CEO review. It is not yet tasked to Luna.*
