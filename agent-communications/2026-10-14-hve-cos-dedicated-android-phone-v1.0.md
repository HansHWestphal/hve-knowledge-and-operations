# Future Engagement: Dedicated Android Phone for HVE-COS / Hermes

**Date:** 2026-10-14  
**Status:** Logged as future engagement / backlog (not yet approved for implementation or hardware purchase)  
**Owner context:** HVE-COS and broader Hermes fleet  
**Source:** Discussion of Phone Harness plugin (ShawnPana/phone-harness) enabling Hermes to control real phones.

## Summary

Give HVE-COS (and the broader Hermes fleet) its own dedicated Android phone as a controlled mobile effector, using the Phone Harness plugin.

This isolates mobile workflows from personal devices and expands Hermes capabilities beyond the desktop/NVIDIA stack into real phone apps and interfaces.

## Context

- Phone Harness (https://github.com/ShawnPana/phone-harness) now has a dedicated Hermes plugin.
- Hermes can see the screen (accessibility tree on Android), open apps, tap/swipe/scroll/type, and continue multi-step tasks inside mobile apps — no per-app API required.
- Android path: ADB over USB or Wi-Fi. No app install or root needed on the phone.
- Install: `hermes plugins install ShawnPana/phone-harness/integrations/hermes`
- Supports iPhone via Mac mirroring and cloud phones as alternatives.

## Proposed scope (future)

1. Acquire a dedicated Android device (used Pixel or solid mid-range recommended) for HVE use only.
2. Enable Developer options + Wireless debugging; pair once via ADB.
3. Install and enable the Phone Harness Hermes plugin on the relevant Hermes runtime(s) (Spark / COS gateway).
4. Define approval / safety boundaries (plugin asks before scripts by default; keep classifier auto-run off initially).
5. Identify first practical HVE workflows (examples: content posting, 2FA / notifications, app testing, client-facing mobile surfaces, monitoring).
6. Document setup, power/docking, network (LAN or Tailscale), and operational runbook.
7. Optional: evaluate running Hermes runtime itself on-device (Termux path) as a complement.

## Why it fits HVE

- Aligns with sovereign / local-first agent stack.
- Gives COS and other agents a real mobile surface without risking personal phones.
- Complements existing Hermes Mobile companion apps and desktop control.

## References

- Phone Harness repo + Hermes integration: https://github.com/ShawnPana/phone-harness
- Related HVE Hermes runtime and COS work already tracked in this repository.

---

Logged from CEO discussion on 2026-10-14. To be reviewed for prioritization against current Hermes / COS work.