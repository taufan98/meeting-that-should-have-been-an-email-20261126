#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — a make.fun entry.

This meeting could have been an email — but the email would have
needed a meeting to explain it. The loop is the joke: the meeting
exists to explain the email that exists to replace the meeting, and
somewhere in that loop an entire afternoon quietly disappears. No
setup paragraph is needed, because everyone reading it has already
lived inside that loop at least once this week.

One line, written to the file the harness reads. Nothing else happens.
"""

from os import environ, makedirs, path

# The entry itself. One line about the meeting that should have been
# an email — and the email that would have needed a meeting anyway.
# The loop is the joke; everyone reading it has lived inside it.
LINE = "This meeting could have been an email, but the email would have needed a meeting to explain it."

# The bounty gate for this entry allows at most 199 characters.
LIMIT = 199


def entry_text():
    """Return the entry line, checked against the bounty gate."""
    text = LINE
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{LIMIT}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    """Write the entry line to the harness output file."""
    out_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(out_dir, exist_ok=True)
    target = path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
