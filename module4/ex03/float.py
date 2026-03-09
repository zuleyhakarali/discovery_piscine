#!/usr/bin/env python3

num = input("Give me a number: ")
for_float = float(num)
if for_float.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")