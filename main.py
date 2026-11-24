#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Gloombury to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

FORECAST = (
    "Gloombury: light drizzle until 9, then sunshine, then a 100% chance "
    "the bus leaves the moment you sit down \u2014 bring a book."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = FORECAST.strip()
    # Gate: the entry must be UTF-8 text of 1 to 140 characters.
    if not (1 <= len(text) <= 140):
        print(f"forecast is {len(text)} characters, must be 1-140", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
