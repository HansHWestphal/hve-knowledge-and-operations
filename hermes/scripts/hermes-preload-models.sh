#!/usr/bin/env bash
# hermes-preload-models.sh
# Spark hot local stack — boot preload for Ollama.
#
# Policy (Hans / HVE Digital Twin, 2026-08-05):
#   Hot local models: qwen3.5:27b-128k, gpt-oss:20b,
#   qwen2.5:3b for Honcho, plus nomic-embed-text
#   Role: Tier A delegation worker complement to cloud Grok 4.5
#   Do NOT preload: nemotron3:33b, 120B, other Qwen sizes, nano/mistral
#   Coding: gpt-oss:20b, Hermes-coder, or GitHub Copilot CLI
#
# Called by: hermes-model-preload.service

set -euo pipefail

OLLAMA_URL="${OLLAMA_URL:-http://127.0.0.1:11434}"
PRIMARY_MODEL="qwen3.5:27b-128k"
PRIMARY_CTX="${PRIMARY_CTX:-131072}"
CODER_MODEL="gpt-oss:20b"
CODER_CTX="${CODER_CTX:-65536}"
EMBEDDING_MODEL="nomic-embed-text"
EMBEDDING_CTX="${EMBEDDING_CTX:-2048}"
DERIVER_MODEL="qwen2.5:3b"
DERIVER_CTX="${DERIVER_CTX:-32768}"
KEEP_ALIVE="${KEEP_ALIVE:--1}"

EVICT_MODELS=(
  "devstral:24b"
  "qwen3-coder:30b"
  "nemotron3:33b"
  "nemotron-3-super:120b"
  "gpt-oss:120b"
  "llama3.3:70b-instruct-q3_K_M"
  "qwen3.5:27b"
  "qwen3.5:9b"
  "qwen2.5-coder:32b"
  "qwen2.5-coder:14b"
  "qwen2.5:14b"
  "mistral-small:24b"
  "nemotron-3-nano:30b"
  "deepseek-r1:32b"
  "deepseek-r1:14b"
  "gemma2:27b"
)

log() { echo "[preload] $*"; }

wait_for_ollama() {
  local retries=90
  log "Waiting for Ollama API at ${OLLAMA_URL}..."
  while ! curl -sf "${OLLAMA_URL}/api/tags" >/dev/null 2>&1; do
    sleep 2
    retries=$((retries - 1))
    if [ "${retries}" -le 0 ]; then
      log "ERROR: Ollama not ready after 180s — aborting"
      exit 1
    fi
  done
  log "Ollama ready."
}

evict_model() {
  local model="$1"
  if command -v ollama >/dev/null 2>&1; then
    if ollama ps 2>/dev/null | awk 'NR>1{print $1}' | grep -qx "${model}"; then
      log "Evicting: ${model}"
      ollama stop "${model}" 2>/dev/null || true
    fi
  fi
}

load_primary() {
  log "Loading primary model: ${PRIMARY_MODEL} (ctx: ${PRIMARY_CTX}, keep_alive: ${KEEP_ALIVE})"
  local response
  response=$(curl -s --max-time 300 "${OLLAMA_URL}/api/generate" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"${PRIMARY_MODEL}\",\"prompt\":\"ok\",\"keep_alive\":${KEEP_ALIVE},\"stream\":false,\"options\":{\"num_ctx\":${PRIMARY_CTX}}}" 2>&1) || true
  if echo "${response}" | grep -qE '"done"[[:space:]]*:[[:space:]]*true|"eval_count"'; then
    log "OK hot: ${PRIMARY_MODEL}"
  else
    log "WARNING: unexpected response for ${PRIMARY_MODEL}"
    echo "${response}" | head -5
  fi
}

load_embedding_model() {
  log "Loading embedding model: ${EMBEDDING_MODEL} (ctx: ${EMBEDDING_CTX}, keep_alive: ${KEEP_ALIVE})"
  local response
  response=$(curl -s --max-time 120 "${OLLAMA_URL}/api/embed" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"${EMBEDDING_MODEL}\",\"input\":\"Hermes embedding warmup\",\"keep_alive\":${KEEP_ALIVE},\"options\":{\"num_ctx\":${EMBEDDING_CTX}}}" 2>&1) || true
  if echo "${response}" | grep -q '"embeddings"'; then
    log "OK hot: ${EMBEDDING_MODEL}"
  else
    log "WARNING: unexpected response for ${EMBEDDING_MODEL}"
    echo "${response}" | head -5
  fi
}

load_coder_model() {
  log "Loading coder model: ${CODER_MODEL} (ctx: ${CODER_CTX}, keep_alive: ${KEEP_ALIVE})"
  local response
  response=$(curl -s --max-time 180 "${OLLAMA_URL}/api/generate" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"${CODER_MODEL}\",\"prompt\":\"ok\",\"keep_alive\":${KEEP_ALIVE},\"stream\":false,\"options\":{\"num_ctx\":${CODER_CTX}}}" 2>&1) || true
  if echo "${response}" | grep -qE '"done"[[:space:]]*:[[:space:]]*true|"eval_count"'; then
    log "OK hot: ${CODER_MODEL}"
  else
    log "WARNING: unexpected response for ${CODER_MODEL}"
    echo "${response}" | head -5
  fi
}

load_deriver_model() {
  log "Loading deriver model: ${DERIVER_MODEL} (ctx: ${DERIVER_CTX}, keep_alive: ${KEEP_ALIVE})"
  local response
  response=$(curl -s --max-time 180 "${OLLAMA_URL}/api/generate" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"${DERIVER_MODEL}\",\"prompt\":\"ok\",\"keep_alive\":${KEEP_ALIVE},\"stream\":false,\"options\":{\"num_ctx\":${DERIVER_CTX}}}" 2>&1) || true
  if echo "${response}" | grep -qE '"done"[[:space:]]*:[[:space:]]*true|"eval_count"'; then
    log "OK hot: ${DERIVER_MODEL}"
  else
    log "WARNING: unexpected response for ${DERIVER_MODEL}"
    echo "${response}" | head -5
  fi
}

print_ps() {
  log "Currently loaded:"
  ollama ps 2>/dev/null || true
}

wait_for_ollama
log "Evicting non-primary models..."
for model in "${EVICT_MODELS[@]}"; do
  evict_model "${model}"
done
sleep 1
load_primary
load_coder_model
load_deriver_model
load_embedding_model
print_ps
log "Done. Hot policy: ${PRIMARY_MODEL}, ${CODER_MODEL}, ${DERIVER_MODEL}, and ${EMBEDDING_MODEL}."
