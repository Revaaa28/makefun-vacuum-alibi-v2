#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters — v2 entry "Acceptable Losses".

Writes the chosen one-line excuse a robot vacuum gives for missing a spot
to /output/entry.txt. Deterministic, stdlib only, no network.

The line: the vacuum did the maths on the corner, decided the crumbs were
not worth dying for, and filed them under acceptable losses. Two numbers
that cross-check (4% in the tank, 6% to reach the corner), deadpan
bureaucrat voice, punch on the last phrase.
"""

import os

ENTRY = "That corner costs 6% battery to reach. I had 4%. I chose survival, and filed your crumbs under 'acceptable losses.'"


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no surrounding space")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, outside the 1-200 limit")


def _write_and_verify(out_dir: str) -> str:
    """Write ENTRY into out_dir, then read it back and check it byte-exactly."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is byte-exactly the one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise OSError(f"read-back mismatch in {path}: {written!r}")
    return path


def write_entry() -> str:
    """Write to /output/entry.txt; if that path fails at any step (missing
    permission, read-only mount, partial write), fall back to ./output."""
    try:
        return _write_and_verify("/output")
    except OSError:
        return _write_and_verify(os.path.join(".", "output"))


def main() -> None:
    validate(ENTRY)
    path = write_entry()
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
