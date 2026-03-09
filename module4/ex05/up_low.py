#!/usr/bin/env python3

s = input()
i = len(s)
for char in s:
    for_char = ord(char)
    if 65 <= for_char <= 90:
        print(chr(for_char + 32), end="")
    elif 97 <= for_char <= 122:
        print(chr(for_char - 32), end="")
    else:
        print(char, end="")
    i -= 1
print()

# YA DA;
#
# print(s.swapcase())
#