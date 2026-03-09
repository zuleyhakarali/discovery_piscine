#!/usr/bin/env python3

import sys

av = sys.argv
i = len(sys.argv)
if i == 1:
    print("none")
    sys.exit(1)
print(f"parameters: {i - 1}")
for j in av[1:]: #0. elemanı atla
    print(f"{j}: {len(j)}")
