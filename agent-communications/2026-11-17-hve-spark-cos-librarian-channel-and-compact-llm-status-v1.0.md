# HVE-COS and HVE-Librarian Channel and Compact LLM Status

- **Date:** 2026-11-17
- **Observed:** 21:23 EDT
- **Prepared by:** Luna, HVE CTO / Head Architect
- **Decision owner:** Hans Westphal, CEO
- **Status:** Current operational status record
- **Scope:** HVE-COS and HVE-Librarian only; HVE-CFO is out of scope

## Outcome

HVE-COS and HVE-Librarian are up and functional on the DGX Spark.

- **HVE-COS:** The managed gateway is active. WhatsApp was successfully
  re-paired through the browser-presented QR flow. The child bridge is
  connected and listening on loopback port `3000`.
- **HVE-Librarian:** The managed gateway is active with its Telegram channel
  enabled. No Librarian configuration or channel state was changed during the
  COS repair.

## Compact-session model

Both profiles now use the following Ollama model for compact-session
compression:

`qwen3.8-distill-4b-128k:latest`

Live Ollama evidence at the observed time showed:

- Model ID: `fc17547842b7`
- Context: `131072`
- Processor: `100% GPU`
- Residency: loaded and available for 24 hours

The primary conversational model remains
`qwen3.8-hermes:27b-128k`; this update changed the compact-session model only.

## Evidence and boundaries

- COS and Librarian systemd user gateways reported `active/running`.
- COS WhatsApp bridge reported `connected` and port `3000` was listening.
- The new COS WhatsApp credentials were written after successful pairing.
- The previous invalidated COS session was preserved as a timestamped backup;
  no session data was deleted.
- No WhatsApp message was sent as part of this recovery.
- No HVE-CFO service, profile, configuration, or channel was modified.

This record describes verified runtime state at the observation time. It is
not a new fleet policy or a claim about historical channel availability before
the repair.
