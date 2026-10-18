#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 innerVANI contributors
# SPDX-License-Identifier: Apache-2.0
"""Check that the frozen runtime pack has not changed.

The runtime pack is the text from "You are a conscience layer" to
"always say what you can do instead." Its fingerprint is the first 16
hexadecimal characters of the SHA-256 hash of that text, encoded as UTF-8,
with LF line endings. The pack appears in two files, and both must match
the published fingerprint.

Usage:
    python scripts/check_fingerprint.py

Exits with status 1 if a file is missing, the pack can't be found in it, or
a fingerprint doesn't match. Changing the pack needs an accepted RFC (see
GOVERNANCE.md), a new pack version and a new fingerprint in this script.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED = "7f0a1936a3528242"  # runtime pack v0.1
START = "You are a conscience layer"
END = "always say what you can do instead."
FILES = ["standard/runtime_pack_v0.1.md", "standard/foundation_v0.1.md"]


def fingerprint(text):
    """Return the fingerprint of the runtime pack inside text."""
    start = text.index(START)
    end = text.index(END, start) + len(END)
    return hashlib.sha256(text[start:end].encode("utf-8")).hexdigest()[:16]


def main():
    failed = False
    for name in FILES:
        path = ROOT / name
        try:
            text = path.read_text(encoding="utf-8")  # reads CRLF line endings as LF
        except FileNotFoundError:
            print(f"FAIL {name}: file not found")
            failed = True
            continue
        try:
            found = fingerprint(text)
        except ValueError:
            print(f"FAIL {name}: can't find the runtime pack (its first or last line is missing)")
            failed = True
            continue
        if found == EXPECTED:
            print(f"ok   {name}: {found}")
        else:
            print(f"FAIL {name}: fingerprint {found}, expected {EXPECTED}")
            failed = True
    if failed:
        print("The runtime pack is frozen. Changing it needs an accepted RFC; see GOVERNANCE.md.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
