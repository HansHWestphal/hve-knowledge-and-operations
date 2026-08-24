# HVE X 333 Quote Skill

**Date:** 2026-08-24
**Owner:** Hermes-coder

## Creation

Created the `x-333-quote` skill for the `hanshermesagent` profile and
preserved its source in the repository under `hermes-skills/x-333-quote/`.

The skill accepts long source passages, typically 500 or more words, extracts
the strongest attributable quote, and returns exactly three quoted lines:

```text
"Author quote"
"Author Name"
"One concise insight to the reader"
```

The complete output is limited to 333 characters. Normal execution uses no
web, shell, code execution, Gmail, Honcho, or skill-library mutation. A
deterministic validator is included.

Honcho stores only the durable formatting preference. Approved outputs may be
added to the HVE knowledge layer separately; drafts are not stored
automatically.
