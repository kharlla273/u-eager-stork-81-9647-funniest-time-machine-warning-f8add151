#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label to /output/entry.txt.

The line (85 chars, within the 1-120 gate):
    NOTICE: Passengers who kill their own grandfather will be charged a cancellation fee.

Why this line, against the judge brief:
  1. It IS a time machine warning label, phrased as a genuine safety notice.
  2. It turns a real hazard of time travel — the grandfather paradox —
     into the joke instead of naming it flatly.
  3. The surprise is saved for the last few words: "cancellation fee"
     lands where the reader least expects it.
  4. It keeps a straight face: deadpan official calm ("will be charged"),
     so the joke cuts against the bureaucratic tone.
  5. No wasted words: every phrase does work inside the character limit.

Deterministic: the same line is written on every run.
"""

import os

ENTRY = "NOTICE: Passengers who kill their own grandfather will be charged a cancellation fee."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
