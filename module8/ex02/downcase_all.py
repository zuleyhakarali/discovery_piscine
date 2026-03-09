#!/usr/bin/env python3

import sys

def downcase_it(s):
    return s.lower()

av = sys.argv
i = len(sys.argv)
if i == 1:
    print("none")
    sys.exit(1)
for j in av[1:]: # buradaki j parametreleri ifade ediyor
    print(downcase_it(j))

"""
j = 1
while j < i: // buradaki j sayısal değeri
    print(downcase_it(av[j]))
    j += 1 
"""