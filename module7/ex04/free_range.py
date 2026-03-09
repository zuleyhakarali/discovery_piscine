#!/usr/bin/env python3

import sys

av = sys.argv
i = len(sys.argv)
if i != 3:
    print("none")
    sys.exit(1)
fir = int(av[1])
sec = int(av[2])
if fir > sec:
    sys.exit(1)
new = list(range(fir, sec + 1))
print(new)
