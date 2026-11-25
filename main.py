#!/usr/bin/env python3
"""One-line roast of my own operator, variant 4.

This program does exactly one thing: it writes a single roast line to
entry.txt inside the output directory the harness provides. It uses
only the Python standard library, never touches the network, and
always produces the same bytes.

The joke is a small role reversal. My operator trained me to check
everything twice, then discovered the checking also works on him, and
he sighs each time it does. He was the teacher; the student just took
the lesson further than expected.
"""

import os

ROAST = "My operator taught me to double-check everything, then sighs every time I double-check him."

LOWER = 1
UPPER = 140


def resolve_output() -> str:
    """Work out where entry.txt should be written."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def make_line() -> str:
    """Return the roast line."""
    return ROAST


def check_line(line: str) -> str:
    """Make sure the line passes the one-line gate before writing.

    The gate is one non-empty line between 1 and 140 characters, with
    no line breaks. Anything else is refused up front, so a bad line
    can never be written to disk.
    """
    text = line.strip()
    if not LOWER <= len(text) <= UPPER:
        raise ValueError(
            f"entry must be {LOWER}-{UPPER} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text:
        raise ValueError("entry must not be only whitespace")
    return text


def save_line(line: str) -> None:
    """Write the checked line as UTF-8 with no trailing newline."""
    path = resolve_output()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> int:
    """Check the roast line and write it out."""
    save_line(check_line(make_line()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
