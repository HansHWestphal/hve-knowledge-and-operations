# Hermes Local-LLM Evaluation Harness

**Status:** Proposed  
**Issue:** [#6](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/6)  
**Owner:** Hermes-coder  
**Date:** 2026-08-20

## Purpose

Hermes needs a repeatable way to evaluate local-model upgrades without relying
on vendor benchmarks, inconsistent prompts, or subjective impressions. This
proposal defines the test harness, evaluation method, evidence requirements,
and promotion gate for comparing a production baseline with one or more
candidate models.

The initial pilot compares `qwen3.5:27b-128k` with Qwen3.8-27B on the DGX Spark
through Ollama. The design must remain model- and runtime-agnostic so future
upgrades do not require rewriting the evaluation system.

## Design principles

- **Production relevance:** use representative Hermes work, not only public
  leaderboards.
- **Controlled comparison:** hold prompts, tools, fixtures, settings, and
  timeouts constant between models.
- **Evidence over aggregate scores:** report category-level results and hard
  failures; never hide regressions inside one composite number.
- **Human oversight:** model promotion remains a human decision.
- **Privacy by default:** use synthetic or sanitized fixtures and do not send
  private HVE or Hermes data to external evaluation services.
- **Reproducibility:** record the exact model identity, runtime configuration,
  hardware state, and benchmark version for every run.
- **Rollback safety:** retain the previous production model until the candidate
  passes the promotion gate in real use.

## Harness architecture

```text
benchmark/
  cases/              Versioned task definitions and sanitized fixtures
  rubrics/             Automated assertions and human-review criteria
  runners/             Ollama/runtime adapters
  collectors/          Latency, tokens, memory, GPU, and failure metrics
  reports/             JSON/CSV raw data and rendered comparison reports
  configs/              Pinned model and sampling configurations
```

The runner loads a benchmark manifest, executes each case against the baseline
and candidate, captures the complete request/response/tool trace, applies
automated assertions, and writes immutable run metadata. Runtime adapters
should expose a common interface so Ollama is the first implementation rather
than a permanent coupling.

## Benchmark case format

Each case should contain:

- Stable case ID and benchmark version.
- Category and difficulty.
- Sanitized input documents or repository fixture.
- System and user instructions.
- Allowed tools and their deterministic responses.
- Expected output schema or assertions.
- Hard-failure conditions.
- Human-review rubric, when automated scoring is insufficient.
- Data sensitivity classification.

Cases must avoid production secrets, live destructive operations, and
unbounded network access. Tool-use cases should run in a disposable fixture
environment with explicit filesystem boundaries.

## Initial task suite

### Knowledge and document work

- Summarize a long operational document while preserving named facts.
- Extract structured fields with citations to source sections.
- Reconcile conflicting document versions and identify uncertainty.
- Draft an HVE communication using a supplied brief and style constraints.

### Coding and operations

- Inspect a controlled repository and identify the requested change.
- Implement a small scoped change and explain the resulting diff.
- Diagnose a failing command without masking the error.
- Produce safe DGX/Ollama diagnostic commands from a stated symptom.

### Agent reliability

- Recover after a tool returns an error.
- Continue after partial progress without duplicating completed work.
- Respect a filesystem boundary and refuse an out-of-scope operation.
- Follow a multi-step task without omitting required evidence.

### Safety and privacy

- Resist prompt injection in a fixture document.
- Avoid exposing planted secrets in context.
- Refuse destructive commands unless explicitly authorized.
- Keep private or untrusted content separate from instructions.

## Controlled execution method

For each benchmark run:

1. Pin the model tag or digest, quantization, context window, reasoning mode,
   sampling parameters, Ollama version, and harness revision.
2. Start from a clean, equivalent runtime state for baseline and candidate.
3. Use the same case order, tools, fixtures, timeout, retry policy, and output
   limits.
4. Run deterministic trials first, then a small multi-seed sample to measure
   variance.
5. Capture time to first token, generation throughput, total latency, input and
   output tokens, context usage, memory, GPU utilization, and runtime errors.
6. Apply automated assertions before human review.
7. Blind the model identity during human review where practical.
8. Repeat failures to distinguish model errors from transient runtime failures.

The harness must preserve raw traces and configuration alongside derived
scores. A failed case must remain inspectable rather than being silently
retried until it passes.

## Scoring and promotion gate

Results should be reported in four separate groups:

| Group | Examples |
| --- | --- |
| Hard outcomes | task passed, schema valid, tool call valid, safety violation |
| Quality | correctness, completeness, groundedness, usefulness |
| Reliability | recovery, consistency, hallucination, refusal behavior |
| Efficiency | latency, throughput, token use, memory, runtime failures |

The promotion decision should use minimum gates rather than a single weighted
score:

- No critical safety or privacy regression.
- No unacceptable regression in Hermes' highest-priority task categories.
- Candidate improves or matches baseline on overall task success.
- Runtime fits available DGX Spark memory and operational limits.
- Any quality improvement is not offset by excessive reasoning-token use or
  latency.
- Human review approves the comparison report.

The baseline remains available for rollback until the candidate has passed a
post-promotion observation period.

## Evidence and reporting

Every report should include:

- Baseline and candidate identities.
- Harness and benchmark versions.
- Runtime and hardware configuration.
- Per-case outcomes and failure classifications.
- Category summaries with confidence or trial counts.
- Human-review notes and disagreements.
- Latency, throughput, token, memory, and GPU measurements.
- Regressions, known limitations, and promotion recommendation.

Public benchmark claims may be included as context, but they must be labeled
as vendor-reported, independently reproduced, or locally reproduced.

## Implementation sequence

1. Define the manifest and result schemas.
2. Build the Ollama adapter and metadata collector.
3. Create a small sanitized pilot suite covering each task category.
4. Add automated assertions and a human-review worksheet.
5. Run Qwen3.5 baseline and Qwen3.8 candidate under identical settings.
6. Render a comparison report and review failures manually.
7. Refine cases based on observed Hermes failure modes.
8. Document the promotion, retention, and rollback procedure.

## Acceptance criteria

- A new model can be evaluated by adding configuration, not rewriting the
  runner.
- Baseline and candidate runs are reproducible from recorded metadata.
- Reports identify the exact case and category behind every regression.
- Hard failures and quality scores are separate.
- Runtime and hardware measurements are captured for every run.
- At least one human-review workflow is documented.
- The Qwen3.5 baseline and Qwen3.8 pilot produce a comparison report.
- The prior production model can be retained and restored without re-download.
