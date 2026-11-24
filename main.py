#!/usr/bin/env python3
"""Write one funny single-line developer excuse to /output/entry.txt.

The entry turns the worn "it worked on my machine" excuse into a fresh
joke: production is the very same machine, only now it has more users,
less memory, and a personal grudge against the developer who shipped it.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "It worked on my machine. Production is the same machine \u2014 just "
    "with more users, less memory, and a personal grudge against me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
