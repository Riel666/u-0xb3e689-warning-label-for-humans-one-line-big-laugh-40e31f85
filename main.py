#!/usr/bin/env python3
"""Write one line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The text is written exactly as given: 128 Unicode code points, inside the
competition gate of 1-160. Python 3.13, standard library only, no network.
"""

import os

# The entry text, byte for byte: no trailing newline, nothing added or cut.
TEXT = "WARNING: contents under pressure. May leak tears at weddings, sneeze three times in a row, and burst into song alone in the car."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
