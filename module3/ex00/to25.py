#!/usr/bin/env python3

import sys
print("Enter a number less than 25")
num = int(input())
if num >= 25:
    print("Error")
    sys.exit(1)
while num < 26:
    print(f"Inside the loop, my variable is {num}")
    num += 1