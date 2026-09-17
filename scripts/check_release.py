# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
"""Release gate (RR-B-15): required files, forbidden paths, forbidden
content, headers present. Exits non-zero on any failure.

Adapted for awesome-stpa (RR-B Base, standalone model): no src/ layout,
no package install, no scripts beyond the gate itself."""
import pathlib
import re
import subprocess
import sys

fails: list[str] = []

REQUIRED = [
    "README.md", "LICENSE", "COPYRIGHT", "NOTICE", "CHANGELOG.md",
    "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "RELEASE-INFO.txt", "CITATION.cff",
    "docs/DISTRIBUTION.md", "docs/index.html",
    "scripts/check_release.py",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         check=True).stdout.splitlines()
FORBIDDEN_PATH_PARTS = ["__pycache__", ".venv", ".worktrees", ".pytest_cache",
                        ".ruff_cache", ".bak"]
for f in tracked:
    if any(part in f for part in FORBIDDEN_PATH_PARTS):
        fails.append(f"forbidden tracked path: {f}")

FORBIDDEN_CONTENT = [re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
                     re.compile(r"CONFIDENTIAL\s+[-—]\s+Not for external distribution")]
SCAN_GLOBS = ["scripts/*.py"]
scanned: set[pathlib.Path] = set()
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        scanned.add(path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rx in FORBIDDEN_CONTENT:
            if rx.search(text):
                fails.append(f"forbidden content in {path}: {rx.pattern}")

HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd"
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        if HEADER_SENTINEL not in path.read_text(encoding="utf-8", errors="ignore")[:600]:
            fails.append(f"header missing: {path}")

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
assert scanned, "scan globs matched nothing; fix SCAN_GLOBS"
print(f"release gate: PASS (scanned {len(scanned)} files)")
