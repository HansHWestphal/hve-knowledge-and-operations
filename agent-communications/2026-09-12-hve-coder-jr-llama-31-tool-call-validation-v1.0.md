# HVE Coder Jr Llama 3.1 Native Tool-Call Validation

**Date:** 2026-09-12  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Native tool-call gate passed; Jr resource and activation gates remain blocked

## Scope and boundaries

This evidence records an isolated evaluation of a newly downloaded model
candidate for `hve-coder-jr`. The production Jr service remained inactive.
The approved Qwen2.5-Coder artifact and configuration were not modified.
Ollama, vLLM, HVE-COS, HVE-Librarian, HVE-CFO, Hermes-Coder live queue/state,
and the Ollama concurrency test were not touched.

## Candidate verification

| Field | Evidence |
|---|---|
| Repository | `bartowski/Meta-Llama-3.1-8B-Instruct-GGUF` |
| Artifact | `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` |
| Path | `/home/hans/models/3rdparty/llama-3.1-8b-instruct/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` |
| Size | `4,920,739,232` bytes |
| SHA256 | `7b064f5842bf9532c91456deda288a1b672397a54fa729aa665952863033557c` |
| GGUF metadata | Llama architecture; 8,030,261,312 parameters; Q4_K - Medium; training context 131072 |
| Embedded template | Llama 3.1 Jinja template; native tool calls; object arguments; no parallel tool calls |
| Runtime | llama.cpp `0.2.0-dev`, build 1, commit `c060ca9`, Linux aarch64 |
| Alias | `llama-3.1-8b-instruct-q4_k_m` |

The upstream `X-Linked-Size` matched the local file. The ARM64 binary opened
the GGUF at 65,536 context with one sequence. The temporary command was:

```text
/home/hans/hve-life-os/src/build/bin/llama-server --model /home/hans/models/3rdparty/llama-3.1-8b-instruct/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf --alias llama-3.1-8b-instruct-q4_k_m --host 127.0.0.1 --port 11435 --ctx-size 65536 --parallel 1 --gpu-layers 999 --flash-attn auto --cache-type-k q8_0 --cache-type-v q8_0 --threads 8 --threads-batch 8 --timeout 120 --metrics --props --slots --jinja --no-warmup --load-mode dio
```

## Native response gate

The deterministic request declared only `read_file`, used temperature `0`,
top-p `1`, seed `7`, `max_tokens` `128`, and `stream: false`. The object
`tool_choice` form returned HTTP 200 and a native call but logged that this
build expects a string and fell back to its default. The supported `"auto"` and
`"required"` forms each returned one native call:

```json
{
  "choices": [{
    "finish_reason": "tool_calls",
    "message": {
      "role": "assistant",
      "content": "",
      "tool_calls": [{
        "type": "function",
        "function": {
          "name": "read_file",
          "arguments": "{\"path\": \"/workspace/README.md\"}"
        },
        "id": "7QNIvf5iMH72vXoaPYEV4yZEQfyVgHgO"
      }]
    }
  }]
}
```

This satisfies the native `message.tool_calls` acceptance target. The
provider-neutral validator accepted the captured fixture and rejects markup,
malformed arguments, invalid names, missing/extra arguments, duplicates,
truncation, and ambiguous content. No returned tool call was executed, and no
text-to-tool adapter was added.

## Resource and activation result

The temporary process returned `/health` HTTP 200, exposed the exact alias from
`/v1/models`, and incremented `/metrics` counters. It reported no usable GPU
in the current llama.cpp binary and measured approximately 9.4 GiB RSS/HWM at
64K context, against Jr’s approximate 8 GiB total runtime budget. Process swap
was zero and memory PSI averages were zero. The candidate is therefore not
eligible to replace the approved Qwen runtime, and Phase E remains blocked on
the resource gate despite native tool-call success.

The temporary process was stopped, port `11435` was clear afterward, and
`hve-coder-jr-llama.service` remained inactive. Production activation remains a
separate approval gate.
