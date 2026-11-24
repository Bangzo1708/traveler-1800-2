#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 (round-2 entry).

Writes a single sentence to /output/entry.txt: one picture, built only
from things a person from 1800 already knows (a post office, a book, a
letter, ink), that explains the modern internet — every book within
reach, and a letter to any door on earth answered before the ink dries.
"""

SENTENCE = (
    "Imagine a post office that holds every book in the world, "
    "where a letter to any door on earth is answered before the ink dries."
)


import os


def main() -> None:
    # The gate allows 1-200 characters; fail loudly instead of ever
    # writing an entry the scorer would refuse.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
