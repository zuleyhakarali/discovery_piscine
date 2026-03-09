#!/usr/bin/env python3

import sys
import re

av = sys.argv
i = len(sys.argv)
if i != 3:
    print("none")
    sys.exit(1)
num = re.findall(av[1], av[2], flags=0)
j = len(num)
if j == 0:
    print("none")
    sys.exit(1)
print(j)
