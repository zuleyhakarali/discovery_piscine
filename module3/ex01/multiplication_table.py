#!/usr/bin/env python3

print("Enter a number")
num = int(input())
multi = 0
new = multi * num
while multi < 10:
    print(f"{multi} x {num} = {new}")
    multi += 1
    new = multi * num