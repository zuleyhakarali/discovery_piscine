#!/usr/bin/env python3

num = [2, 8, 9, 48, 8, 22, -12, 2]
i = 0
j = len(num)
new = set()
while j > i:
    if num[i] > 5:
        new.add(num[i] + 2)
    i += 1
print(num)
print(new)