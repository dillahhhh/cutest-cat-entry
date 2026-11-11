#!/usr/bin/env python3
"""Draw the cutest cat: writes the entry image to /output/entry.png."""
import os, shutil
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"
os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
print("wrote", DST)
