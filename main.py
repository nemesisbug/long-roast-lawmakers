#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt: lawmakers write the
rules for crypto, AI and the whole internet, then cannot turn a Word
file into a PDF. The program checks its own output against the gate
(1-320 characters, UTF-8, not only whitespace, a single sentence)
before writing it.
"""

import os
import sys

ENTRY = (
    "They wrote the rules for crypto, AI and the whole internet into a "
    "400-page bill, then sent it to the clerk as a phone photo of a "
    "laptop screen because no one in the building could turn a Word "
    "file into a PDF."
)

MAX_CHARS = 320


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"gate fail: {len(text)} characters (must be 1-{MAX_CHARS})",
              file=sys.stderr)
        return 1
    if text != text.strip():
        print("gate fail: leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate fail: entry must be exactly one sentence",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
