#!/usr/bin/env python3
"""Validate the fixed x-333-quote output contract."""

from __future__ import annotations

import sys


MAX_CHARS = 333


def main() -> int:
    text = sys.stdin.read().rstrip("\n")
    lines = text.splitlines()
    valid_shape = (
        len(lines) == 3
        and all(line.startswith('"') and line.endswith('"') for line in lines)
    )
    if not valid_shape:
        print("invalid: expected quoted quote, author, insight on exactly three lines")
        return 1
    if len(text) > MAX_CHARS:
        print(f"invalid: {len(text)} characters exceeds {MAX_CHARS}")
        return 1
    print(f"valid: {len(text)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
