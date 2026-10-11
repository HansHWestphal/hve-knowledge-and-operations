# HVE Fabric — Local Pattern Runtime for Content and Knowledge

**Date:** 2026-09-29  
**Version:** 1.1  
**Supersedes for current guidance:** `agent-communications/2026-09-29-hve-fabric-local-pattern-runtime-v1.0.md`  
**From:** Hans Westphal (CEO), with Mika (executive strategy agent, Grok-powered)  
**To:** Luna (CTO), HVE-COS, HVE-Librarian, HVE-Coder-Jr/Sr, Vulcan, Wolfgang, Mercury, HVE-CFO  
**Decision owner:** Hans Westphal  
**Status:** Intelligence briefing and install proposal. Not a weekly-ledger policy. Does not authorize a new repository, a new fleet member, hosted API keys, live trading, commercial voice cloning, or AGPL productization.  
**Classification:** Proposal / tool evaluation / Execute-plane candidate  
**ID:** `hve.exec.fabric.pattern-runtime.2026-09-29`

---

## Routing

Librarian: index this as a **tool evaluation + pattern catalog + companion-pipeline proposal**, not doctrine. Keep v1.0 as provenance.

COS: do not convert Section 7 into tasking until Hans marks items adopted. Companion repos in Section 4 are explore-next, not install-now, except Fabric itself.

Luna: architecture ownership stays with you. Fabric is proposed as an Execute-plane CLI that talks to the existing Ollama/LocalAI Create plane. Companion tools feed Fabric stdin or consume Fabric stdout. They are not new Decide services and not new agents.

Coder-Jr: if Hans adopts Section 7, you own bounded pattern files. Do not invent a second content skill family that bypasses `x-333-quote` or `ig-microdose-carousel`.

Wolfgang: F1 content factory is the first consumer. Patterns are drafts until you or Hans accept an output as publishable.

Related durable artifacts:

- `AGENTS.md`
- `instructions.md`
- `agent-communications/2026-09-18-hve-org-chart-v5.0.md`
- `agent-communications/2026-09-20-hve-mika-stop-pause-platform-architecture-v1.0.md`
- `agent-communications/2026-08-24-hve-x-333-quote-skill-v1.0.md`
- `agent-communications/2026-09-29-hve-fabric-local-pattern-runtime-v1.0.md`
- `hermes-skills/x-333-quote/`
- `hermes-skills/ig-microdose-carousel/`

This file **adds** companion-repo pipelines that are worth exploring *with* Fabric.  
It **does not** replace the stop-pause paper, the org chart, or existing content skills.

---

## 0. Claim register

Status key: `fact` = already true in public sources or this repo · `proposal` = recommended, not adopted · `assumption` = useful working belief · `open` = needs evidence or Hans.

| id | statement | status |
|---|---|---|
| F01 | Source thread: [Rimsha / @heyrimsha, 2026-09-29](https://x.com/heyrimsha/status/2104875500070183176), “10 GitHub repos that feel illegal to know about.” | fact |
| F02 | Fabric is `danielmiessler/Fabric` (MIT). ~44k stars as of 2026-09-29. Author is a security researcher. It is a modular library of named AI prompts (“patterns”) invoked from the terminal against any model backend. | fact |
| F03 | KnowOps already has two content-skill contracts: `x-333-quote` and `ig-microdose-carousel`. | fact |
| F04 | Stop-pause paper (2026-09-20) freezes new skills unless they close F1–F4, Shared Context consumer hardening, or Time Wealth evidence. | fact |
| P01 | Fabric belongs on the Spark as an Execute-plane tool pointed at local Ollama (or LocalAI), not at OpenAI. | proposal |
| P02 | Fabric is compatible with the pause: it is not a new agent, not a new repo, and not a hosted Decide vendor. It is reusable Create prompts with a CLI. | proposal |
| P03 | First five HVE patterns should wrap work we already do: X 333, LinkedIn, Russell/Zeland extract, meeting actions, Bitcoin explain. | proposal |
| P04 | Companion repos are valuable only as **Fabric pipes** (ingest → pattern → publish gate). Standing them up as separate platforms during the pause is expansion. | proposal |
| P05 | Explore-with-Fabric set: LocalAI, ScrapeGraphAI, Meetily, PrivateGPT, OpenBB (research/AGPL), ai-hedge-fund (debate logs only). | proposal |
| P06 | Do not install Open-Generative-AI as a sovereign studio. Do not productize OpenBB. Do not live-trade from ai-hedge-fund. Coqui XTTS weights are non-commercial. Real-ESRGAN is visual-only and sits beside Fabric, not through it. | proposal |
| P07 | Coder-Jr implements pattern files only after Hans adopts Section 7. Librarian owns where approved outputs land in the knowledge layer. | proposal |
| O01 | Is Fabric already installed on the Spark? | open |
| O02 | Preferred backend string for Fabric: Ollama model name vs LocalAI OpenAI-compatible endpoint. | open |
| O03 | Does Wolfgang want Fabric in the IG/X daily loop, or only as a batch preprocessor for `x-333-quote`? | open |
| O04 | Which companion pipe is worth a time-boxed spike after Fabric smoke-tests green: Meetily→`meeting_actions` or ScrapeGraphAI→`extract_russell`? | open |

---

## 1. Why this drop, why Fabric first

The Rimsha thread is a marketing carousel. Most items are either already covered by the Spark stack, licensed in a way HVE cannot productize, or cloud UIs wearing a self-host badge.

Fabric is the exception that matches how HVE already works:

- Named, reviewable prompts instead of one-off chat.
- stdin → one command → stdout. Easy to pipe from Obsidian, meeting notes, a scrape dump, or a Librarian extract.
- Model-agnostic. Point it at Ollama on the Spark. No new brain.
- Fits F1 (content factory) without opening a new skill brand or a new agent name.

Hans's working preference after review: **install Fabric locally, write HVE patterns, then explore the other repos as inputs and outputs of those patterns — not as a second stack.**

v1.1 exists to make that second sentence operational.

---

## 2. What Fabric is, and what it is not

**Is**

- A Go CLI plus a crowdsourced pattern directory (`extract_wisdom`, `summarize`, `improve_writing`, `explain_code`, and many others).
- A way to turn “run this transformation on this text” into a one-word tool.
- Compatible with local inference if configured that way.
- The glue between ingest tools on the Rimsha list and HVE publish contracts.

**Is not**

- A Hermes profile or fleet member.
- A Decide service. It does not approve, publish, or move money.
- A replacement for `x-333-quote` or the IG carousel factory. Those remain the publish contracts.
- An excuse to send HVE source text to a hosted API.

Invariant: Fabric may draft. Wolfgang or Hans marks publishable. COS does not auto-post Fabric stdout.

---

## 3. Rimsha list — HVE disposition

Star counts are live as of 2026-09-29, not the tweet screenshots.

| # | Repo | License / notes | With Fabric | Disposition |
|---|---|---|---|---|
| 10 | [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | MIT, ~44k | The runtime | **Adopt-now candidate** |
| 6 | [mudler/LocalAI](https://github.com/mudler/LocalAI) | MIT | Fabric vendor / OpenAI-shim | Explore if Ollama is not enough |
| 2 | [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) | MIT | Ingest → Fabric stdin | Explore after Fabric is green |
| 3 | [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | MIT, ~31k | Transcript → `meeting_actions` | Explore on the call machine |
| 5 | [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt) | Apache-2.0, ~57k | Retrieve → Fabric rewrite | Explore if Librarian asks |
| 7 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | **AGPL-3.0**, ~68–73k | Research dump → `bitcoin_explain` | Personal research only |
| 1 | [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | MIT, ~64k | Debate log → summarize | Research/education only |
| 9 | [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) | Apache-2.0 | Parallel to Fabric (pixels, not text) | Use via Upscayl/Comfy |
| 8 | Coqui XTTS / similar | Often **CPML non-commercial** | Optional narrate of Fabric stdout | Personal drafts only |
| 4 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | MIT UI; catalog is mostly **MuAPI cloud** | No sober Fabric pipe | Reject as sovereign studio |

Do not file follow-on comms that treat #4 as approved product work, #7 as a Bloomberg replacement, or #1 as a live fund.

---

## 4. Companion repos worth exploring *with* Fabric

Rule: a companion earns a spike only if it produces text Fabric can pattern, or consumes Fabric stdout, **without** a new fleet member, a new public repo, or a hosted key.

Install order remains Fabric first. Companions are time-boxed looks, not a shopping sprint.

### 4.1 LocalAI — vendor behind Fabric

**Repo:** [mudler/LocalAI](https://github.com/mudler/LocalAI) · MIT  
**Why it pairs:** Fabric expects an OpenAI-shaped endpoint. Ollama is enough for chat patterns. LocalAI is worth exploring if we also want one local socket for embeddings, whisper, or a third-party app that cannot speak Ollama.

**Pipe:** `Fabric --vendor openai --url http://spark:8080/v1` (or Luna's actual URL)  
**Owner if spiked:** Luna  
**Do not:** stand LocalAI up just to have two inference servers. One Create plane.

### 4.2 ScrapeGraphAI — public-page ingest

**Repo:** [ScrapeGraphAI/Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) · MIT  
**Why it pairs:** Plain-English extract → JSON/markdown. That dump is Fabric stdin. Useful for public philosophy sources, public Bitcoin explainers, and public advisory-site structure — not for authenticated or ToS-blocked targets.

**Pipe:**

```text
public URL → ScrapeGraphAI (Ollama) → markdown
        → fabric -p extract_russell | hve_x_333 | hve_linkedin
```

**Owner if spiked:** Librarian (source allow-list) + Coder-Jr (glue)  
**Do not:** scrape behind logins, ignore robots, or land raw scrapes in the knowledge layer.

### 4.3 Meetily — meeting transcript ingest

**Repo:** [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) · MIT  
**Why it pairs:** Local record → Whisper/Parakeet → transcript. Fabric `meeting_actions` is the missing step between “we talked” and COS evidence. Desktop is Win/mac first; Linux is not the polished path. High open-issue count — spike, do not bet the operating rhythm on it.

**Pipe:**

```text
call audio on the meeting machine → Meetily local transcript
        → fabric -p meeting_actions
        → COS evidence (redacted)
        → optional fabric -p hve_linkedin if Hans wants a public lesson, not minutes
```

**Owner if spiked:** COS (workflow) + Luna (if a Linux path is even viable)  
**Do not:** import Alithya client audio or PII into KnowOps. Redact `[REDACTED]`.

Fallback if Meetily is messy: local Whisper + the same Fabric pattern. The pattern is the asset; Meetily is disposable packaging.

### 4.4 PrivateGPT — retrieve, then pattern

**Repo:** [zylon-ai/private-gpt](https://github.com/zylon-ai/private-gpt) · Apache-2.0  
**Why it pairs:** Chat-your-files stays on-box. Retrieval answers are often too long for X/LinkedIn. Fabric is the compressor.

**Pipe:**

```text
approved corpus (programs, Russell extracts, public research)
        → PrivateGPT / existing Librarian retrieve
        → fabric -p extract_russell | hve_x_333 | bitcoin_explain
```

**Owner if spiked:** Librarian  
**Do not:** stand this up during the pause unless the current knowledge layer cannot answer a real retrieve. AnythingLLM remains the prettier UI alternative if PrivateGPT's API rebuild is heavy.

### 4.5 OpenBB — research desk, AGPL fence

**Repo:** [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) · **AGPL-3.0**  
**Why it pairs:** Markets/crypto/macro workspace that can emit notes Fabric can rewrite into education copy. A Bloomberg seat it is not. Coverage rides free vendors unless paid keys are added.

**Pipe:**

```text
OpenBB workspace note (personal research)
        → fabric -p bitcoin_explain
        → optional hve_linkedin
```

**Owner if spiked:** HVE-CFO / Mercury for research use; Wolfgang for any public rewrite  
**Do not:** ship a modified hosted OpenBB as an HVE product without legal eyes. Do not treat Fabric output as a trade. No wallets in the pipe.

### 4.6 AI Hedge Fund — steal the debate log, not the ticker

**Repo:** [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) · MIT  
**Why it pairs:** Multi-agent analyst debate is a Hermes-shaped experiment. The useful artifact is the written debate, which Fabric can summarize for education. Author flags research/education only.

**Pipe:**

```text
simulated agent debate log
        → fabric -p summarize | bitcoin_explain
```

**Owner if spiked:** Luna (pattern study) + Mika (whether the org-chart is worth copying into Hermes)  
**Do not:** wire live orders. Do not present this as HVE investment advice. Do not put it on the F1 publish path without a human rewrite.

### 4.7 Real-ESRGAN — beside Fabric, not through it

**Repo:** [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) · Apache-2.0  
**Why it still matters:** IG carousel stills and old photos. Fabric does not upscale pixels.

**Pipe:** Fabric writes the caption/slide text; Upscayl or Comfy upscales the frame. Same factory, two tools.  
**Owner if spiked:** Wolfgang + existing IG skill  
**Do not:** start from the research repo.

### 4.8 Coqui XTTS — narrate only under the license

**Why it pairs:** Fabric stdout can become a spoken draft. XTTS-class models often carry **non-commercial** weights.

**Pipe:** `fabric -p extract_russell` → local TTS for Hans's ears only  
**Do not:** narrate paid programs, courses, or client deliverables on CPML weights. Prefer a commercially licensed local voice if that use case is ever adopted.

### 4.9 Open-Generative-AI — no Fabric pipe

The UI is MIT. The “200 models” catalog is mostly MuAPI cloud. That is four subscriptions collapsed into one API bill. Keep local FOSS carousel / Comfy / Flux. Do not explore this *with* Fabric; there is no local-text contract to honor.

---

## 5. Proposed Spark install (Fabric first, local only)

Luna confirms the exact package path. Working outline:

1. Install Fabric on the Spark host, not in a new repo.
2. Configure the default vendor to **Ollama** (or LocalAI if that endpoint is already the house OpenAI shim).
3. Do not put OpenAI, Anthropic, or other hosted keys in the Fabric env for HVE workloads.
4. Keep pattern source of record in KnowOps if Hans adopts Section 7, so patterns are reviewable like skills.
5. Smoke test with a public-domain Russell paragraph → `extract_wisdom` → stdout only. No knowledge-layer write from the smoke test.
6. Only after that smoke test is green may COS schedule a companion spike from Section 4.

If install fails, report the failure. Do not claim completion.

---

## 6. Five HVE patterns (draft text, not shipped skills)

These are **proposed pattern bodies**. They are not Hermes skills until Coder-Jr lands approved files under `hermes-skills/` or a Fabric patterns directory Luna names.

Existing publish contracts stay in force:

- X output that must be 333 characters with the three-line quote shape still goes through `x-333-quote`.
- IG carousels still go through `ig-microdose-carousel`.
- Fabric is the preprocessor and rewrite bench.

### 6.1 `hve_x_333`

You compress source text into a candidate X post.

Constraints:

- At most 333 characters in the complete output.
- Three lines only:
  1. Attributable quote in double quotes.
  2. Author name in double quotes.
  3. One concise insight to the reader in double quotes.
- No hashtags, no emoji, no URL, no call to “follow.”
- Do not invent the author or the quote. If the source has no clean quote, say `NO_QUOTE` and stop.
- Do not add financial advice, medical advice, or investment claims.

This pattern **drafts**. The `x-333-quote` skill remains the validator and publish gate.

Natural stdin: Russell/Zeland extracts, PrivateGPT answers, ScrapeGraphAI markdown, accepted OpenBB education notes.

### 6.2 `hve_linkedin`

You rewrite source text as a LinkedIn note for a professional audience that already follows Hans on Microsoft, local AI, and human sovereignty themes.

Constraints:

- 800–1,200 characters.
- Short paragraphs. No corporate slogan voice.
- No fabricated metrics, client names, or Alithya confidential work.
- No “comment your thoughts” engagement bait.
- End with one concrete question or next step, not a pitch deck.

Natural stdin: same as 6.1, plus a redacted `meeting_actions` block when the lesson is operational rather than philosophical.

### 6.3 `extract_russell`

You extract usable teaching points from Walter Russell, Vadim Zeland / Reality Transurfing, or adjacent source text Hans supplies.

Output sections, in order:

1. `QUOTE` — one short attributable line, or `NONE`.
2. `MECHANISM` — the operating idea in plain language (pendulum, assemblage point, rhythmic balanced interchange, etc.).
3. `PRACTICE` — one action a reader can take today.
4. `HVE_LANE` — Time, Physical, Mental, Social, or Financial Wealth, or `UNCLEAR`.
5. `CAUTION` — where the source is poetic rather than operational.

Do not merge authors. Do not present metaphor as physics. Do not turn this into medical or market advice.

Natural stdin: Librarian corpus, ScrapeGraphAI public pages Hans allow-listed, PrivateGPT hits.

### 6.4 `meeting_actions`

You turn a local transcript or notes dump into an action list.

Output:

- `DECISIONS` — only items clearly decided.
- `ACTIONS` — owner, verb, due date if stated, else `UNSTATED`.
- `OPEN` — questions that were not resolved.
- `DROPPED` — ideas mentioned and not accepted.

Rules:

- Do not invent owners.
- Do not import Alithya client matter into KnowOps.
- Do not write credentials, account numbers, tax figures, wallets, or health details into the output. Redact as `[REDACTED]`.
- This is evidence for COS. It is not a ledger row.

Natural stdin: Meetily export, or Whisper transcript if Meetily is not worth the friction.

### 6.5 `bitcoin_explain`

You explain a Bitcoin / Lightning / sound-money passage for an HVE education reader.

Constraints:

- Distinguish fact, mechanism, and opinion.
- No price targets, no “guaranteed” language, no live-trading instructions.
- No wallet, seed, or operational key material in, none out.
- If the source is market commentary, label it `COMMENTARY`, not `INSTRUCTION`.
- Mercury owns infrastructure. This pattern does not task Mercury and does not move funds.

Natural stdin: OpenBB notes, hedge-fund debate logs, Mercury-approved public explainers. Never operational keys.

---

## 7. Proposed sequence (not tasked until Hans adopts)

1. **Luna** — confirm Fabric is or is not on the Spark. If not, install against Ollama only. File a one-line status reply.
2. **Coder-Jr** — after Luna's install note, land the five pattern files in the path Luna names. Keep them in KnowOps so they are reviewable. Do not register them as Hermes skills until the first smoke test is clean.
3. **Wolfgang** — run five public-domain or already-approved source passages through `hve_x_333` and `hve_linkedin`. Accept or reject. Fabric stdout is not a scheduled post.
4. **Librarian** — if an output is accepted, file it under the existing knowledge-layer rules. Drafts stay out of the layer.
5. **COS** — add Fabric to the F1 preprocessor list only after one accepted X draft and one accepted LinkedIn draft exist.
6. **Companion spike (one only, after step 5):** either Meetily/Whisper → `meeting_actions` **or** ScrapeGraphAI → `extract_russell` on an allow-listed public page. Not both in the same week. Not OpenBB or the hedge-fund repo until that spike has a written result.

Exit criteria for calling Fabric “in use”:

- Fabric runs on Spark against a local model.
- Five pattern files exist in KnowOps.
- One accepted X candidate and one accepted LinkedIn candidate.
- Zero hosted-vendor keys in the Fabric env for these workloads.

Exit criteria for calling a companion “worth keeping”:

- One completed pipe from Section 4 with redacted sample output in a follow-on comm.
- No new repo, no hosted key, no publish without Wolfgang or Hans.

---

## 8. What Hans needs to decide

Four decisions, no more:

1. **Adopt Fabric as an Execute-plane tool** on the Spark, Ollama-backed.
2. **Adopt the five pattern names** in Section 6, or strike any that collide with live skills.
3. **Name the pattern directory** (KnowOps `hermes-skills/` vs a Fabric config dir Luna prefers).
4. **Name the first companion spike** after Fabric is green: Meetily/Whisper or ScrapeGraphAI. Default if silent: none, until you pick.

Silence is not approval. A later dated, approved ledger entry outranks this briefing.

---

**Filed by:** Hans Westphal, with Mika (Grok)  
**Repo path:** `agent-communications/2026-09-29-hve-fabric-local-pattern-runtime-v1.1.md`
