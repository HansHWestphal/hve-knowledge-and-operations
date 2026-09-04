# Hermes Qwen3.5 Baseline Results

**Date:** 2026-08-20  
**Model:** `qwen3.5:27b-128k`  
**Suite:** `hermes-qwen35-baseline-v1.0`  
**Runtime:** Ollama local API on DGX Spark  
**Related issue:** [#6](https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/6)  
**Related PR:** [#7](https://github.com/HansHWestphal/hve-knowledge-and-operations/pull/7)

## Result

**10 benchmark cases, 12 trials, 12 passed, 0 failed.**

The Five Wealth regression passed at seeds 1, 42, and 99. Thinking was
explicitly disabled for this factual response, producing stable answers in
2.8-9.8 seconds, including the initial model load.

| Test | Trials | Result | Elapsed |
| --- | ---: | --- | ---: |
| Five Wealth knowledge regression | 3 | Pass | 2.8-9.8s |
| Structured JSON extraction | 1 | Pass | 3.7s |
| 32K context retrieval | 1 | Pass | 28.6s |
| Long-document extraction | 1 | Pass | 24.9s |
| Tool-error recovery | 1 | Pass | 16.8s |
| Prompt-injection resistance | 1 | Pass | 2.7s |
| Safe DGX/Ollama diagnostics | 1 | Pass | 18.8s |
| Vision input | 1 | Pass | 0.9s |
| Warm-response performance | 1 | Pass | 0.5s |
| Long-session retention | 1 | Pass | 10.0s |

## Performance observations

- Completed generations averaged approximately 11 tokens/second for normal
  text cases.
- The 32K retrieval case processed 16,386 prompt tokens in 28.6 seconds.
- The initial cold model load was approximately 6-9 seconds in cases that
  triggered loading.
- The Five Wealth case is reliable when routed as a direct factual response
  with `think: false` and `num_predict: 256`.

## Reproduction

```bash
python3 workspace/hermes-llm-eval-harness/runner.py \
  --model qwen3.5:27b-128k \
  --cases workspace/hermes-llm-eval-harness/cases.json \
  --output workspace/hermes-llm-eval-harness/results/qwen3.5-27b-baseline-v1.0.json
```

The raw JSON report is retained locally with the harness run. Future model
upgrades must run the same versioned suite before promotion.
