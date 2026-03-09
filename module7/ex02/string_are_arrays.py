#!/usr/bin/env python3

import sys

av = sys.argv
i = len(sys.argv)
if i != 2:
    print("none")
    sys.exit(1)
s = av[1]
j = 0
counter = 0
while j != len(s):
    if s[j] == 'z':
        print("z", end="")
        counter += 1
    j += 1
if counter == 0:
    print("none")
else:
    print()