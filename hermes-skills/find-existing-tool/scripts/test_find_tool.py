#!/usr/bin/env python3
"""Offline self-test for find_tool.py. Uses a synthetic index in a temp dir; no network.

Run: python3 scripts/test_find_tool.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "find_tool.py"

FIXTURE = [
    {"name": "LLM4Decompile", "url": "https://github.com/a/llm4decompile", "desc": "Models that decompile binaries",
     "category": "RE Tooling", "subcategory": "Disassemblers & Decompilers", "stars": 7000,
     "pushed": "2026-02-12", "archived": False, "lang": "Python", "license": "MIT", "topics": []},
    {"name": "ghidra-helper", "url": "https://github.com/a/ghidra-helper", "desc": "Explains functions with LLMs",
     "category": "RE Tooling", "subcategory": "AI-assisted RE", "stars": 50,
     "pushed": "2026-10-01", "archived": False, "lang": "Java", "license": "GPL-3.0", "topics": []},
    {"name": "dllmaker", "url": "https://github.com/a/dllmaker", "desc": "Builds Windows DLL files",
     "category": "File Formats", "subcategory": "Other", "stars": 10,
     "pushed": "2020-01-01", "archived": False, "lang": "C", "license": "", "topics": []},
    {"name": "psd-parser", "url": "https://github.com/a/psd-parser", "desc": "Parser for PSD files",
     "category": "File Formats", "subcategory": "Design Tools (PSD, Sketch, Figma, Affinity)", "stars": 300,
     "pushed": "2025-06-01", "archived": False, "lang": "Python", "license": "MIT", "topics": []},
    {"name": "chat2api", "url": "https://github.com/a/chat2api", "desc": "Turns a chatbot website into an OpenAI-compatible LLM API",
     "category": "AI Tools & LLM Clients", "subcategory": "Chatbot Web APIs", "stars": 9000,
     "pushed": "2026-10-01", "archived": False, "lang": "Go", "license": "MIT", "topics": []},
    {"name": "prompt-leaks", "url": "https://github.com/a/prompt-leaks", "desc": "Leaked system prompts of LLM products",
     "category": "AI Tools & LLM Clients", "subcategory": "System Prompt Leaks & Extractions", "stars": 9000,
     "pushed": "2026-10-01", "archived": False, "lang": "", "license": "", "topics": []},
    {"name": "old-archived-llm-tool", "url": "https://github.com/a/old", "desc": "LLM tool, archived",
     "category": "RE Tooling", "subcategory": "Other", "stars": 5, "pushed": "2019-01-01",
     "archived": True, "lang": "Python", "license": "MIT", "topics": []},
]


class FindToolTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = Path(self.tmp.name) / "cache"
        self.fixture = Path(self.tmp.name) / "entries.json"
        self.fixture.write_text(json.dumps(FIXTURE))
        self.env = dict(os.environ, HVE_RE_INDEX_HOME=str(self.home), PYTHONDONTWRITEBYTECODE="1",
                        https_proxy="http://127.0.0.1:9", http_proxy="http://127.0.0.1:9",
                        HTTPS_PROXY="http://127.0.0.1:9", HTTP_PROXY="http://127.0.0.1:9")
        self.assertEqual(self.run_tool("refresh", "--from-file", str(self.fixture), "--min-entries", "5").returncode, 0)

    def tearDown(self):
        self.tmp.cleanup()

    def run_tool(self, *args, env=None):
        return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True,
                              env=env or self.env, timeout=60)

    def search(self, *args):
        r = self.run_tool("search", *args, "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)

    def names(self, *args):
        return [x["name"] for x in self.search(*args)["results"]]

    def test_short_term_prefix_expansion(self):
        n = self.names("llm")
        self.assertIn("LLM4Decompile", n)          # llm -> llm4...
        self.assertIn("ghidra-helper", n)          # llm -> LLMs
        self.assertNotIn("dllmaker", n)            # no mid-word match

    def test_plural_expansion(self):
        self.assertIn("psd-parser", self.names("parsers"))

    def test_risky_hidden_by_default(self):
        out = self.search("llm")
        names = [x["name"] for x in out["results"]]
        self.assertNotIn("chat2api", names)
        self.assertNotIn("prompt-leaks", names)
        self.assertGreaterEqual(out["hidden_risky"], 2)
        shown = self.names("llm", "--show-risky")
        self.assertIn("chat2api", shown)
        self.assertIn("prompt-leaks", shown)

    def test_flags_and_health(self):
        res = {x["name"]: x for x in self.search("llm", "--show-risky", "--include-archived")["results"]}
        self.assertIn("TOS_LLM_WEB_API", res["chat2api"]["flags"])
        self.assertIn("LEAKED_CONTENT", res["prompt-leaks"]["flags"])
        self.assertIn("LICENSE_NONE", res["prompt-leaks"]["flags"])
        self.assertIn("LICENSE_COPYLEFT", res["ghidra-helper"]["flags"])
        self.assertEqual(res["old-archived-llm-tool"]["health"], "archived")
        self.assertNotIn("old-archived-llm-tool", self.names("llm"))  # archived excluded by default

    def test_invalid_refresh_keeps_last_good(self):
        bad = Path(self.tmp.name) / "bad.json"
        bad.write_text("{not json")
        r = self.run_tool("refresh", "--from-file", str(bad), "--min-entries", "5")
        self.assertEqual(r.returncode, 2)
        self.assertIn("kept last-good", r.stderr)
        self.assertIn("LLM4Decompile", self.names("llm"))

    def test_shrink_and_min_count_rejected(self):
        small = Path(self.tmp.name) / "small.json"
        small.write_text(json.dumps(FIXTURE[:2]))
        self.assertEqual(self.run_tool("refresh", "--from-file", str(small), "--min-entries", "1").returncode, 2)
        self.assertEqual(self.run_tool("refresh", "--from-file", str(small), "--min-entries", "5").returncode, 2)

    def test_second_refresh_keeps_prev(self):
        self.assertEqual(self.run_tool("refresh", "--from-file", str(self.fixture), "--min-entries", "5").returncode, 0)
        self.assertTrue((self.home / "entries.prev.json").exists())
        self.assertTrue((self.home / "meta.json").exists())

    def test_offline_search_works(self):
        r = self.run_tool("search", "decompile")  # proxies point at a dead port
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("LLM4Decompile", r.stdout)

    def test_clone_requires_confirm(self):
        r = self.run_tool("clone", "a/psd-parser")
        self.assertEqual(r.returncode, 3)
        self.assertIn("--confirm", r.stderr)

    def test_clone_refuses_unlisted_and_in_repo(self):
        self.assertEqual(self.run_tool("clone", "evil/not-listed", "--confirm").returncode, 3)
        r = self.run_tool("clone", "a/psd-parser", "--confirm", "--dest", str(HERE / "vendor" / "x"))
        self.assertEqual(r.returncode, 3)

    def test_tokens_never_used(self):
        fakebin = Path(self.tmp.name) / "bin"
        fakebin.mkdir()
        marker = Path(self.tmp.name) / "gh-called"
        (fakebin / "gh").write_text(f"#!/bin/sh\ntouch {marker}\necho FAKE_TOKEN\n")
        (fakebin / "gh").chmod(0o755)
        env = dict(self.env, GITHUB_TOKEN="ghp_should_never_be_used", GH_TOKEN="x",
                   PATH=f"{fakebin}{os.pathsep}{self.env.get('PATH', '')}")
        for args in (("search", "llm"), ("info", "a/psd-parser"), ("status",)):
            r = self.run_tool(*args, env=env)
            self.assertNotIn("ghp_should_never_be_used", r.stdout + r.stderr)
        self.assertFalse(marker.exists(), "gh was invoked")
        probe = subprocess.run([sys.executable, "-c",
                                "import sys,os; sys.argv=['x','status']; sys.path.insert(0, %r); "
                                "import find_tool; print(os.environ.get('GITHUB_TOKEN'), os.environ.get('GH_TOKEN'))"
                                % str(HERE)], capture_output=True, text=True, env=env)
        self.assertEqual(probe.stdout.strip(), "None None")

    def test_cache_inside_skill_dir_refused(self):
        env = dict(self.env, HVE_RE_INDEX_HOME=str(HERE / "cache"))
        r = self.run_tool("status", env=env)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("inside the skill directory", r.stderr + r.stdout)

    def test_vendored_hash_ok(self):
        r = self.run_tool("status", "--json")
        self.assertTrue(json.loads(r.stdout)["vendored_sha256_ok"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
