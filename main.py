"""Write the built front page where the harness expects it.

Standard library only, no network, no randomness. The image is drawn
by tools/build_image.py and committed here as entry.png; this script
copies it to the output directory (OUTPUT_DIR, or /output by default).
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    if not os.path.isfile(SRC):
        print("error: entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
