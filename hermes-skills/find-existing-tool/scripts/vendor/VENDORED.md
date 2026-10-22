# Vendored: `re_index.py`

| Field | Value |
|---|---|
| Upstream repo | https://github.com/alexgaoth/awesome-reverse-engineered |
| Upstream path | `plugin/skills/find-reverse-engineered/scripts/re_index.py` |
| Vendored from commit | `586cffd011070efff6875b3f3921b05637f67786` (main, "Nightly refresh 2026-10-21 (#37)") |
| Last upstream change to this file | `0fd48394be8490ac83dbe2754aa39d892ffc40a2` (2026-10-14, "Move the Claude plugin into plugin/ …") |
| sha256 | `5cad537f25fde5a094888e11e1c89d24ae5f17c81564c4ef784460ca2131234b` |
| License | MIT, Copyright (c) 2026 Alex Gao. Full text in [`LICENSE-UPSTREAM`](LICENSE-UPSTREAM), taken from the same commit. |
| Data license | The index data (`data/entries.json`) is CC0 1.0 (upstream `LICENSE-DATA`). It is **not** vendored; it is downloaded into a cache outside the repo. |
| Vendored on | 2026-10-21 by HVE Knowledge Ops |

## Notes
- The file is byte-for-byte identical to upstream. `find_tool.py` checks the sha256 and warns on mismatch. Do not edit it in place; put HVE behaviour in `find_tool.py`.
- History: upstream licensed the code CC0 until 2026-10-14. Commit `9c1e8af371a2673fd7f00f3c0b3785bcb0133a5a` relicensed the code to MIT and moved CC0 to the data. This file did not change in that commit.
- `find_tool.py` only imports `fields()` (field weights) and `SYNONYMS` from this module. It never calls upstream `load()` (network refresh) or `github_readme()`, which can read a token via `gh auth token`.

## Updating the pin
1. Read the upstream diff for this path since the pinned commit.
2. Replace `re_index.py`, then update `UPSTREAM_COMMIT` and `VENDORED_SHA256` in `../find_tool.py` and this table.
3. Run `python3 scripts/test_find_tool.py`.
4. Commit with the new SHA in the message.
