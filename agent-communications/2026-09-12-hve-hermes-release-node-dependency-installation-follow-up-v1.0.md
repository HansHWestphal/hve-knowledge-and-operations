# HVE Hermes Release Node Dependency Installation Follow-up

**Date:** 2026-09-12  
**Owner:** Luna, HVE CTO / Head Architect  
**Status:** Backlog  
**Related operational item:** Spark Hermes WhatsApp health summary, attention item 2

## Issue

The Hermes runtime release process activates Python release worktrees but does
not automatically install or verify Node dependencies for the WhatsApp bridge.
This allowed the live Baileys bridge to start without its optional peer
dependency `link-preview-js`, producing runtime link-preview failures even
though the package was present in the bridge lockfile.

The immediate dependency repair is live in Hermes release
`62b989c2058d5c1e7b79599996136a13cf2c30ca`. This backlog item tracks the
deployment reliability improvement rather than the already-completed package
repair.

## Required follow-up

Update the managed Hermes release workflow so every release that contains the
WhatsApp bridge:

1. Runs `npm ci --omit=dev` from the release's
   `scripts/whatsapp-bridge/` directory before activation.
2. Fails closed when dependency installation fails.
3. Verifies that the bridge can import its required runtime dependencies,
   including `link-preview-js`.
4. Records the dependency-install result in the release validation evidence.
5. Preserves the existing known-good release and rollback path when validation
   fails.

## Acceptance evidence

- A newly staged release starts the bridge from its own release directory with
  a complete dependency tree.
- `npm ls --depth=0` succeeds for the bridge.
- A local Baileys link-preview smoke test succeeds without sending a WhatsApp
  message.
- A failed Node dependency install prevents activation and leaves the previous
  release active.

## Constraints

- Do not use ad-hoc installation into only the currently active release as the
  permanent solution.
- Do not run `npm audit fix` as part of this follow-up; dependency upgrades
  require a separate review.
- Keep WhatsApp bridge dependency changes isolated from COS, Librarian, CFO,
  and Hermes-Coder behavior.
