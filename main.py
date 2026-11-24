#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (160 chars) pitching a bizarre startup idea to
/output/entry.txt. Deterministic: the same bytes on every run.
Standard library only.
"""

import os

ENTRY = (
    "We rent out professional ghosts to haunt your Airbnb, because hosts pay "
    "$50 a night for the only amenity guests photograph, five-star, and "
    "rebook to meet again."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
