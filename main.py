#!/usr/bin/env python3
"""The Moon Gets One Star - a one-star review of the Moon in under 120 chars.

Writes the review to /output/entry.txt for the make.fun judge.
Pure stdlib, deterministic, no network, no secrets.
"""
import os

# The review: the Moon is receding from Earth at about 3.8 cm a year,
# and has been for roughly 4 billion years. Sparred against ghosting,
# werewolf, tide and eclipse angles; the drift fact is the most
# surprising grievance, and the line ends on the joke word.
REVIEW = (
    "1 star: leaving at 3.8cm a year for 4 billion years. "
    "Sir, that's not an orbit, that's a breakup."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(REVIEW)


if __name__ == "__main__":
    main()
