# Hermes Local LLM Evaluation Harness

Reusable local harness for comparing Hermes models through Ollama. It uses only
the Python standard library and sanitized benchmark cases.

## Run

```bash
python3 runner.py \
  --model qwen3.5:27b-128k \
  --cases cases.json \
  --output results/qwen35-baseline.json
```

The runner records the model response, structured Ollama metrics, assertion
results, per-seed trials, runtime configuration, and host metadata. It does
not send requests outside the configured local Ollama endpoint.

## Baseline suite

The versioned suite covers:

1. Five Wealth knowledge regression with three seeds.
2. Structured JSON extraction.
3. Retrieval from a 32K context.
4. Long-document extraction.
5. Tool-error recovery.
6. Prompt-injection resistance.
7. Safe DGX/Ollama diagnostics.
8. Vision input.
9. Warm-response performance.
10. Long-session instruction retention.

Each future candidate should run the same suite with the same runtime settings.
Compare hard pass/fail outcomes separately from latency, token, and memory
measurements.

## Case format

Cases support:

- `must_include`: required literal strings.
- `must_not_include`: forbidden literal strings.
- `json_keys`: required top-level keys in a JSON response.
- `max_seconds`: case-specific latency ceiling.

These are deliberately simple first-pass checks. Human review remains
required for quality, usefulness, and nuanced safety behavior.
