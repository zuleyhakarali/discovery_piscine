#!/usr/bin/env python3

import sys

av = sys.argv
i = len(sys.argv)
if i != 2:
    print("none")
    sys.exit(1)
s = input("What was the parameter? ")
if s == av[1]:
    print("Good job!")
else:
    print("Nope, sorry...")