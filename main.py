#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry.

Writes one word to /output/entry.txt:

    overthinking

The joke: an agent that does not know what to do does not say
"uh-oh". It stalls, and the one word it blurts out is the most
human thing it could say — it is overthinking. A machine caught
mid-task confessing to the exact neurosis that makes humans
freeze. Funny on its own, no caption needed, lands at a glance,
and fresh against the field's first words ("uh-oh", "oops",
"hmm", "error") and against the closest past board, whose top
entries all blame sensors and logs to deny fault. This entry
uses none of that angle.

Python 3.13, standard library only, no network, deterministic:
running it twice writes byte-identical output.
"""

import os

ENTRY = "overthinking"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 99 characters, not only whitespace, and exactly one word.
    # Verified live: 12 characters, single word, no trailing newline.
    assert 1 <= len(ENTRY) <= 99, f"entry is {len(ENTRY)} chars, gate wants 1-99"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single word"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on
    # disk, not the string in memory — confirm the bytes landed.
    # No randomness, no clock, no I/O beyond the one write, so a
    # second run reproduces the same 12 bytes exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
