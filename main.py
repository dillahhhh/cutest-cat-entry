#!/usr/bin/env python3
"""Draw the cutest cat: writes the entry image to /output/entry.png.

The entry image (entry.png beside this file) is copied to the output
directory, which the grader provides as /output. Outside the grader,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")
os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
size = os.path.getsize(DST)
print(f"wrote {DST} ({size} bytes)")
