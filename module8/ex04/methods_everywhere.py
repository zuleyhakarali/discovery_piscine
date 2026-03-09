#!/usr/bin/env python3

def shrink(s):
    print(s[:8])

def enlarge(s):
    #i = len(s)
    #i = 8 - i
    #print(s + (i * 'Z'))
    #YA DA;
    print(s.ljust(8, 'Z'))

import sys

av = sys.argv
i = len(sys.argv)
if i == 1:
    print("none")
    sys.exit(1)
for j in av[1:]:
    ln = len(j)
    if ln > 8:
        shrink(j)
    elif ln < 8:
        enlarge(j)
    else:
        print(f"{j}")