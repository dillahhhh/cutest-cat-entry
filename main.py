#!/usr/bin/env python3
"""Draw the cutest cat: writes the entry image to /output/entry.jpg.

The entry image (entry.jpg beside this file) is copied to the output
directory, which the grader provides as /output. Outside the grader,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.jpg")
if not os.path.isfile(SRC):
    sys.exit(f"missing entry image: {SRC}")
with open(SRC, "rb") as fh:
    if fh.read(8) != b"\x89PNG\r\n\x1a\n":
        sys.exit(f"entry image is not a PNG: {SRC}")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
size = os.path.getsize(DST)
print(f"wrote {DST} ({size} bytes)")
