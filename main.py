#!/usr/bin/env python3
"""Entry for Fix Human Sleep: Funniest Patch Note (u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27).

Writes one line (max 200 characters) for the judge to /output/entry.txt:
the brief's ask, landed in a single read, grounded and specific. No network,
no randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "Patch note for human sleep v2.0: removed 3 AM anxiety dialogs, snooze button now escalates to a supervisor dream, REM is now distributed."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
