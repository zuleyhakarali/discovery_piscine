#!/usr/bin/env python3

num = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {num}")
i = 0
j = len(num)
while j > 0:
   num[i] = num[i] + 2
   i += 1
   j -= 1
print(f"New array: {num}")