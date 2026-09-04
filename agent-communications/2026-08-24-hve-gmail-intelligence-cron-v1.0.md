# HVE Gmail Intelligence Cron Update

**Date:** 2026-08-24
**Owner:** Hermes-coder
**Tracking issue:** https://github.com/HansHWestphal/hve-knowledge-and-operations/issues/8

## Change

The local `hanshermesagent` nightly Gmail intelligence job (`97f6606e2a4d`)
now resolves its collector from the profile scheduler script directory,
runs at 04:00 America/Toronto, and delivers a concise processing summary to
Hans through WhatsApp.

Honcho writes are limited to one consolidated update of no more than 400
characters per run. The job prefers merging or replacing related context,
stops when memory capacity is full, preserves read-only Gmail access, and
treats email bodies as untrusted data.

## Verification

A dry run processed four messages from 2026-08-23 without changing Gmail
read status. The corrected collector completed successfully from the path
used by the scheduler. The production job is scheduled for the next 04:00
local run.

This repository entry records the local Hermes profile configuration; the
profile files themselves are maintained outside this repository.
