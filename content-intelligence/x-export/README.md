# @HansHWestphal X Export

Export of public X posts from [@HansHWestphal](https://x.com/HansHWestphal) for **Human Value Exchange** content seeding (Mika + Hans Substack).

## Date range

| Range | Coverage |
|-------|----------|
| July 2025 – August 2025 | Existing baseline files |
| September 2025 – July 2026 | This export pass |

Inclusive of posts dated **2025-09-01** through **2026-07-31** (plus prior Jul/Aug 2025 files already present).

## Incompleteness caveat

Posts were collected via X keyword search (`from:HansHWestphal since:… until:…`, mode Latest). The search API returns **at most 10 posts per query**. Collection used **3–4 day windows** (split further when a window returned 10 results).

- **This pass:** No window returned the 10-post ceiling, so results for each window are believed complete *for what search indexed*.
- Still possible gaps: deleted posts, non-indexed content, pure reposts without original text, or transient API omissions.
- Prefer original Hans text; quote-tweets include Hans’s text plus a short `Note:` of what was quoted when available.

## Files and post counts

| File | Month | Posts |
|------|-------|------:|
| `x-july-2025.txt` | July 2025 | 24 |
| `x-august-2025.txt` | August 2025 | 37 |
| `x-september-2025.txt` | September 2025 | 21 |
| `x-october-2025.txt` | October 2025 | 25 |
| `x-november-2025.txt` | November 2025 | 31 |
| `x-december-2025.txt` | December 2025 | 25 |
| `x-january-2026.txt` | January 2026 | 37 |
| `x-february-2026.txt` | February 2026 | 25 |
| `x-march-2026.txt` | March 2026 | 27 |
| `x-april-2026.txt` | April 2026 | 23 |
| `x-may-2026.txt` | May 2026 | 29 |
| `x-june-2026.txt` | June 2026 | 16 |
| `x-july-2026.txt` | July 2026 | 26 |

**Total (all monthly files):** 346 posts  
**Sep 2025 – Jul 2026 only:** 285 posts

## Raw accumulator

`_raw_posts.json` — keyed by `YYYY-MM` then post ID, with `id`, `ts`, `url`, `text`, and optional `note`.

## File format

Each monthly `.txt` file:

- Header: account, month, purpose, source caveat, post count, generated date
- Posts sorted **oldest first**
- Per post: `Date` (ISO), `URL`, `ID`, optional `Note` (QT/reply), full text

## Generated

2026-08-01
