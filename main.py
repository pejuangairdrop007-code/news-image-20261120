#!/usr/bin/env python3
"""Entry point: copy the pre-drawn poster to the output directory.

Standard library only; no network, no randomness. The image is drawn by
gen_image.py at build time and shipped in this repository as entry.png.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy size mismatch")
    print("wrote", dst)


if __name__ == "__main__":
    main()
    sys.exit(0)
