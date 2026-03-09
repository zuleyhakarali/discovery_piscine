#!/usr/bin/env python3

import sys

av = sys.argv
i = len(sys.argv)
if i <= 2:
    print("none")
else:
    while i > 1:
        print(f"{av[i - 1]}")
        i -= 1
