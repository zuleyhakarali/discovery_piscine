#!/usr/bin/env python3

import sys

av = sys.argv
i = len(sys.argv)
if i == 1:
    print("none")
for j in av[1:]:
    idx = j.find("ism")
    if idx == -1:
        print(f"{j}ism")