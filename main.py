#!/usr/bin/env python3
"""One Word From Grandma: the single word grandma would text about AI.

Grandma doesn't say "artificial intelligence". She texts about her
COMPOOTER -- the loving misspelling she has used for thirty years,
now aimed at the clever new machine that answers her questions.
Warm, a little baffled, funny in a single word, and unmistakably
about the machine on her kitchen table.
"""

import os

WORD = "COMPOOTER"


def _check_gate(word: str) -> None:
    """Enforce the competition gate before writing anything out."""
    if not 1 <= len(word) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(word)}")
    if not word.strip() or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word, not blank")
    if not word.isalpha():
        raise ValueError("entry must be plain letters, no punctuation tricks")


def main() -> None:
    _check_gate(WORD)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
