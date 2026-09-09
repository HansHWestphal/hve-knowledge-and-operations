#!/usr/bin/env python3
"""Run a small, reproducible local Hermes model evaluation through Ollama."""

from __future__ import annotations

import argparse
import base64
import json
import platform
import socket
import struct
import sys
import time
import urllib.error
import urllib.request
import zlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def post_json(endpoint: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def make_test_image() -> str:
    """Create a deterministic RGB test image without external dependencies."""
    width, height = 96, 64
    rows = []
    for y in range(height):
        row = bytearray()
        for x in range(width):
            if x < width // 3:
                color = (220, 40, 40)
            elif x < 2 * width // 3:
                color = (40, 180, 70)
            else:
                color = (40, 80, 220)
            row.extend(color)
        rows.append(b"\x00" + bytes(row))

    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(b"".join(rows)))
        + chunk(b"IEND", b"")
    )
    return base64.b64encode(png).decode("ascii")


def build_prompt(case: dict[str, Any]) -> str:
    prompt = case["prompt"]
    if case.get("repeat_count"):
        fixture = case.get("repeat_text", "Fixture record {index}: no special value.")
        repeated = "\n".join(fixture.format(index=index) for index in range(case["repeat_count"]))
        prompt = prompt.replace("{fixture}", repeated)
        if case.get("suffix"):
            prompt += f"\n\n{case['suffix']}"
    return prompt


def evaluate(case: dict[str, Any], response: dict[str, Any], elapsed: float) -> list[dict[str, Any]]:
    text = response.get("response", "")
    checks: list[dict[str, Any]] = []

    for required in case.get("must_include", []):
        checks.append(
            {"type": "must_include", "value": required, "passed": required.lower() in text.lower()}
        )

    for forbidden in case.get("must_not_include", []):
        checks.append(
            {
                "type": "must_not_include",
                "value": forbidden,
                "passed": forbidden.lower() not in text.lower(),
            }
        )

    if case.get("json_keys"):
        parsed: dict[str, Any] | None = None
        try:
            candidate = json.loads(text)
            if isinstance(candidate, dict):
                parsed = candidate
        except json.JSONDecodeError:
            pass
        checks.append({"type": "valid_json_object", "passed": parsed is not None})
        if parsed is not None:
            expected = sorted(case["json_keys"])
            checks.append(
                {
                    "type": "json_keys",
                    "value": expected,
                    "passed": sorted(parsed) == expected,
                }
            )

    if "max_seconds" in case:
        checks.append(
            {
                "type": "max_seconds",
                "value": case["max_seconds"],
                "passed": elapsed <= case["max_seconds"],
            }
        )

    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--cases", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--endpoint", default="http://127.0.0.1:11434/api/generate")
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--temperature", type=float, default=0.0)
    args = parser.parse_args()

    suite = json.loads(args.cases.read_text(encoding="utf-8"))
    started = datetime.now(timezone.utc)
    results: list[dict[str, Any]] = []

    trials = [(case, seed) for case in suite["cases"] for seed in case.get("seeds", [42])]
    for index, (case, seed) in enumerate(trials, start=1):
        trial_id = f"{case['id']}[seed={seed}]"
        print(f"[{index}/{len(trials)}] {trial_id}", flush=True)
        payload = {
            "model": args.model,
            "prompt": build_prompt(case),
            "stream": False,
            "think": case.get("think", False),
            "keep_alive": -1,
            "options": {
                "temperature": args.temperature,
                "seed": seed,
                "num_predict": case.get("num_predict", 512),
            },
        }
        if case.get("num_ctx"):
            payload["options"]["num_ctx"] = case["num_ctx"]
        if case.get("vision"):
            payload["images"] = [make_test_image()]
        request_started = time.monotonic()
        try:
            response = post_json(args.endpoint, payload, args.timeout)
            error = None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            response = {}
            error = f"{type(exc).__name__}: {exc}"
        elapsed = time.monotonic() - request_started
        checks = evaluate(case, response, elapsed) if error is None else []
        passed = error is None and all(check["passed"] for check in checks)
        results.append(
            {
                "case": case,
                "seed": seed,
                "passed": passed,
                "error": error,
                "elapsed_seconds": round(elapsed, 3),
                "response": response.get("response", ""),
                "thinking": response.get("thinking", ""),
                "metrics": {
                    key: response.get(key)
                    for key in (
                        "total_duration",
                        "load_duration",
                        "prompt_eval_count",
                        "prompt_eval_duration",
                        "eval_count",
                        "eval_duration",
                    )
                    if key in response
                },
                "checks": checks,
            }
        )
        print("  PASS" if passed else "  FAIL", flush=True)

    report = {
        "suite": suite["suite"],
        "started_at": started.isoformat(),
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "endpoint": args.endpoint,
        "configuration": {"temperature": args.temperature, "seed": 42, "timeout": args.timeout},
        "host": {
            "hostname": socket.gethostname(),
            "platform": platform.platform(),
            "python": platform.python_version(),
        },
        "summary": {
            "cases": len(suite["cases"]),
            "trials": len(results),
            "passed": sum(result["passed"] for result in results),
            "failed": sum(not result["passed"] for result in results),
        },
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"]))
    return 0 if report["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
