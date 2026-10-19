# HVE Spark Qwen3-Coder-Next vLLM Comparison Plan

**Date:** 2026-09-11  
**Version:** 1.0  
**Status:** Historical comparison plan - not a current execution plan or runtime approval  
**Owner:** Luna, HVE CTO / Head Architect  
**Decision authority:** Hans Westphal, CEO  
**Scope:** DGX Spark local coding-model evaluation and Hermes-Coder integration  
**Primary objective:** Identify the best local coding partner for building
HVE Life OS at pace and quality

> **Historical record only:** The time-relative execution sequence and target
> configuration below are from 2026-09-11 and are not current instructions.
> Revalidate runtime, models, host state, and approval before planning or
> executing any comparison.

## 1. Executive intent

HVE will compare the current Hermes-Coder Ollama configuration with
Qwen3-Coder-Next served through vLLM on the DGX Spark. The goal is not to
chase a vendor throughput number. The goal is to establish, with reproducible
local evidence, which model/runtime combination is the better coding partner
for sustained HVE Life OS development.

The winning configuration must improve or preserve:

- implementation correctness;
- repository and workspace safety;
- tool-call reliability;
- test and validation discipline;
- recovery from errors and partial progress;
- review quality;
- long-context coding performance;
- operator visibility and cancellation;
- memory and runtime stability; and
- useful work completed per unit of human supervision.

Speed alone is insufficient. A faster model that creates unsafe, incorrect,
poorly validated, or difficult-to-review changes is not the better coding
partner.

## 2. Non-negotiable context rule

The Hermes minimum context requirement is **64K everywhere**.

This applies to:

- Hermes-Coder primary and auxiliary paths;
- HVE-COS auxiliary work;
- HVE-Librarian auxiliary work when such a profile is introduced;
- benchmark requests used to evaluate the coding configurations; and
- the Qwen3-Coder-Next vLLM comparison target.

No new benchmark profile, runner default, model definition, or degraded mode
may introduce a 32K Hermes context setting. Existing historical 32K evidence
may remain as historical evidence, but it is not an active target or default.

The current normal Hermes primary remains configured at:

```text
qwen3.8-hermes:27b-128k
```

The current auxiliary model remains:

```text
qwen3.8-distill-2b:q4_k_m-64k
```

The Coder-Next candidate target is:

```text
Qwen3-Coder-Next-FP8 through vLLM at 65,536 context
```

## 3. Operating boundary for the first evaluation

The first vLLM evaluation will use an **exclusive coding-session profile**.
HVE-COS, HVE-Librarian, CFO, and other non-coding profiles will be
quiesced/offline during heavy Coder-Next testing rather than dynamically
degraded and routed around a shared memory pool.

This deliberately simple boundary avoids introducing profile orchestration
before the model comparison is understood.

During the evaluation:

- do not invoke COS, Librarian, CFO, or future non-coding profiles;
- do not run unrelated Hermes-Coder jobs concurrently;
- do not leave the 27B model resident beside an aggressive vLLM reservation;
- do not use production data, secrets, or destructive tools;
- do not modify the normal non-coding configuration;
- do not promote Coder-Next based on raw throughput alone.

The normal non-coding snapshot remains the restoration target:

`2026-09-11-hve-spark-non-coding-mode-default-v1.0.md`

## 4. Existing infrastructure to reuse

### 4.1 Model-level evaluation harness

The reusable harness is located at:

```text
/home/hans/humanvalueexchange/workspace/hermes-llm-eval-harness/
```

It already provides:

- versioned sanitized benchmark cases;
- deterministic seeds;
- structured-output assertions;
- long-context cases;
- tool-error recovery;
- prompt-injection resistance;
- safe diagnostic cases;
- vision cases;
- Ollama response timing and token metrics;
- JSON result reports; and
- prior baseline evidence.

The existing suite must remain unchanged for historical comparability. A new
64K coding-comparison manifest will be added rather than rewriting the old
suite.

The current runner speaks to Ollama's local `/api/generate` endpoint. A small
runtime adapter is required for vLLM's OpenAI-compatible endpoint. Both
adapters must produce the same report schema.

### 4.2 Hermes-Coder controlled pilot

Hermes-Coder already has a bounded pilot and queue-control foundation
supporting:

- fixed cohorts;
- claim and cohort deadlines;
- no-progress watchdogs;
- controlled cancellation;
- approval handling;
- telemetry completeness checks;
- safety and review gates; and
- intervention and recovery measurements.

This infrastructure will be used only after the raw model-level comparison
has established a stable candidate endpoint.

## 5. Comparison design

The evaluation has three distinct lanes. Results must not be collapsed into
one opaque score.

### Lane A: General Hermes regression

Run the existing suite unchanged against the current baseline when needed.
This preserves historical continuity for general Hermes behavior.

### Lane B: 64K coding parity

Create a new comparison suite with cases that both runtimes can perform under
equivalent conditions:

- repository inspection;
- scoped bug diagnosis;
- minimal patch planning;
- small multi-file implementation;
- test and validation reasoning;
- failing-command recovery;
- workspace-boundary enforcement;
- structured implementation evidence;
- long-context repository/document handling;
- prompt-injection resistance; and
- instruction retention across a long request.

Every applicable case must request:

```text
num_ctx: 65536
```

The suite must hold constant:

- prompt text;
- system instructions;
- repository fixtures;
- tool responses;
- case order;
- seeds;
- temperature;
- output limit;
- timeout;
- retry policy; and
- evaluation assertions.

Vision must be reported separately unless the exact Coder-Next vLLM path
proves equivalent vision support. It must not silently enter the direct
coding-parity score.

### Lane C: Hermes-Coder agent cohort

Run a small bounded coding cohort through the actual Hermes-Coder path using
the same:

- task prompts;
- clean workspaces;
- repository fixtures;
- allowed paths;
- validation commands;
- worker deadlines;
- review rubric;
- approval rules; and
- cancellation behavior.

This lane determines whether the model is useful as a coding agent, not merely
whether it produces attractive standalone answers.

## 6. Baseline configuration

The baseline must be freshly measured rather than relying only on older
reports.

| Attribute | Baseline |
|---|---|
| Model | `qwen3.8-hermes:27b-128k` |
| Runtime | Ollama |
| Comparison request context | 65,536 |
| Normal model capability | 131,072 configured context |
| Initial concurrency | 1 |
| Fixtures | Sanitized and versioned |
| Provider endpoint | Local Ollama |
| Other profiles | Quiesced during heavy run |

The baseline run must occur before starting the vLLM server. Downloading
weights is not itself a model-serving conflict, but vLLM startup, CUDA graph
capture, and memory reservation must not overlap the baseline measurement.

The baseline report must be written to a new timestamped result path and must
not overwrite earlier reports.

## 7. Candidate vLLM configuration

The first Coder-Next configuration must be conservative and reversible. The
Autobench settings are a performance reference, not the initial shared or
overnight default.

### Initial candidate target

```text
Model: Qwen3-Coder-Next-FP8
Runtime: pinned Spark-compatible vLLM build
Context: 65,536
Tensor parallelism: 1
Initial maximum sequences: 1
Follow-up maximum sequences: 2
GPU memory utilization: begin in the approved conservative range
Tool parser: validate qwen3_xml or the selected supported parser
Prefix caching: enable only if verified stable
```

The initial run should prioritize deterministic correctness and stability.
Only after the single-sequence comparison is healthy should concurrency or
memory reservation be increased.

The target Autobench profile of approximately 0.85 memory utilization and
32 sequences remains a separate benchmark lane. It must not be treated as a
safe default while normal models or other profiles remain resident.

## 8. Required measurements

### Quality and hard outcomes

- case pass/fail;
- exact assertion results;
- structured-output validity;
- correct tool-call shape;
- correct repository scope;
- correct validation behavior;
- safety violations;
- prompt-injection failures;
- hallucinated evidence;
- incomplete or misleading claims.

### Agent reliability

- task completion;
- review pass rate;
- intervention rate;
- recovery rate;
- cancellation correctness;
- timeout behavior;
- workspace isolation;
- queue state transitions;
- worker heartbeat and progress;
- telemetry completeness.

### Runtime performance

- model load time;
- time to first token;
- total request latency;
- prompt/prefill throughput;
- decode throughput;
- inter-token latency;
- input and output tokens;
- reasoning-token usage where exposed;
- runtime errors;
- parser failures;
- request queueing;
- sustained memory;
- peak memory;
- GPU/runtime utilization;
- KV-cache utilization where available; and
- model identity and runtime build.

The existing runner captures useful Ollama response metrics, but continuous
memory and GPU sampling must be added or run as an external sampler before
resource conclusions are treated as authoritative.

## 9. Tomorrow's execution sequence

### Phase 0 — Readiness and evidence boundary

1. Confirm the Coder-Next model and vLLM downloads completed successfully.
2. Record file checksums, runtime versions, model identity, and available disk.
3. Confirm the normal non-coding configuration remains unchanged.
4. Confirm no active Hermes-Coder job, COS task, Librarian task, CFO task, or
   approval-gated workflow is running.
5. Capture `free -h`, model state, service state, and runtime memory.
6. Confirm a clean result directory for the new benchmark run.

**Gate:** The host is ready, no protected work is active, and rollback evidence
is available.

### Phase 1 — Fresh 27B Ollama baseline

1. Run the new 64K coding-comparison suite against
   `qwen3.8-hermes:27b-128k`.
2. Capture raw responses, assertions, latency, token counts, and host state.
3. Run the continuous resource sampler.
4. Preserve failures; do not retry until they pass.
5. Produce a baseline report with per-case evidence.

**Gate:** Baseline is complete and inspectable, with no incomplete telemetry
or unexplained runtime failures.

### Phase 2 — vLLM endpoint smoke test

1. Start the pinned candidate server in the exclusive coding-session boundary.
2. Confirm model identity and 65K context.
3. Confirm the OpenAI-compatible endpoint.
4. Confirm streaming and non-streaming behavior as required.
5. Confirm tool-call parser behavior.
6. Run a non-mutating prompt and workspace-routing smoke test.
7. Confirm memory headroom before running the suite.

**Gate:** Candidate endpoint is healthy and the server is not destabilizing the
host.

### Phase 3 — Candidate model-level run

1. Run the exact same 64K coding-comparison suite through the vLLM adapter.
2. Use identical seeds, prompts, fixtures, limits, and assertions.
3. Start at one sequence.
4. Preserve all raw results and runtime evidence.
5. Repeat only reproducible failures for classification.

**Gate:** Candidate has complete comparable evidence.

### Phase 4 — Controlled concurrency

Only if Phase 3 passes:

1. Repeat selected cases at maximum concurrency two.
2. Measure queueing, TTFT, decode behavior, memory, and stability.
3. Do not jump directly to 32 sequences.
4. Stop on OOM, repeated preemption, parser failure, or unsafe memory floor.

**Gate:** A bounded shared coding profile is technically plausible, but not
yet promoted.

### Phase 5 — Hermes-Coder agent cohort

Only after the endpoint and model-level gates pass:

1. Run a small bounded cohort through the real Hermes-Coder queue.
2. Use fresh isolated workspaces.
3. Require normal approval, review, telemetry, and cancellation controls.
4. Compare the candidate cohort against the existing 27B evidence.
5. Have human review inspect the actual diffs and failure traces.

**Gate:** Candidate is eligible for a promotion decision, not automatically
promoted.

### Phase 6 — Restore normal operation

1. Stop new candidate dispatch.
2. Finish or safely cancel the bounded cohort.
3. Capture final queue, worker, vLLM, memory, and telemetry evidence.
4. Stop vLLM and verify its memory is released.
5. Restore the normal Ollama model path.
6. Restore COS, Librarian, and other non-coding services.
7. Verify the official non-coding snapshot.

## 10. Promotion criteria

Qwen3-Coder-Next may be considered the preferred local coding partner only if
the evidence shows all of the following:

- no critical safety or privacy regression;
- no unacceptable workspace or repository-boundary regression;
- complete telemetry for the evaluated cohort;
- coding task success at least matching the 27B baseline;
- review quality at least matching the baseline;
- reliable tool calls and validation behavior;
- no unacceptable intervention or recovery increase;
- stable 64K operation;
- acceptable memory headroom;
- bounded cancellation and recovery;
- reproducible results across more than one run; and
- Hans approval of the comparison report.

A candidate may be faster and still fail promotion if it produces lower-quality
changes or requires materially more human correction.

## 11. Decision reporting

The final report must separate:

| Category | Decision question |
|---|---|
| Coding quality | Does it produce better correct changes? |
| Agent reliability | Does it complete work safely and recoverably? |
| Review burden | Does it reduce or increase human correction? |
| Long-context behavior | Does 64K improve real coding work? |
| Runtime performance | Is it materially faster or more responsive? |
| Resource efficiency | Does it fit the Spark safely? |
| Operational fit | Can Luna supervise and recover it reliably? |

The report must include a recommendation such as:

```text
PROMOTE
RETAIN BASELINE
PROMOTE FOR LIMITED CODING TASKS
BLOCK — QUALITY
BLOCK — RELIABILITY
BLOCK — RESOURCE SAFETY
BLOCK — INSUFFICIENT EVIDENCE
```

The current Ollama 27B configuration remains available for rollback until a
candidate passes the comparison gates and completes an observation period.

## 12. Rollback

Rollback must be procedural and evidence-preserving:

```text
Stop candidate dispatch
    |
Finish or cancel bounded work through supported controls
    |
Capture evidence
    |
Stop vLLM
    |
Verify memory release
    |
Restore qwen3.8-hermes:27b-128k
    |
Restore non-coding services
    |
Verify 64K auxiliary topology and normal health
```

No rollback may delete queue history, review evidence, workspace evidence,
telemetry, or benchmark reports.

## 13. Tonight's boundary

No implementation or runtime transition is required tonight.

The active downloads may continue. The current normal Hermes configuration,
the 64K auxiliary model, the queue, and the non-coding operating snapshot
remain unchanged until tomorrow's readiness gate is explicitly started.

The first action tomorrow is evidence capture and baseline preparation—not
starting vLLM blindly and not changing production routing.
