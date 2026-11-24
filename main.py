"""Everyday Things, Two Lines — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 254-character two-line explanation: line 1 tells a
10-year-old that a toaster is a tiny sunbathing bed for bread, and line 2
says why the analogy works — heat plus timing — and what it leaves out,
that bread cannot choose when to get up. It stays under the 400-character
limit, two lines exactly.
"""

import os

ENTRY = 'A toaster is a tiny sunbathing bed for bread: it lies under hot wires until it turns golden, then pops up when it is done.\nThe analogy works because both use heat and timing, but it leaves out that bread cannot choose when to get up — the spring decides.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 400  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry exactly as defined above — verbatim, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
