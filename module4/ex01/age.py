#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
i = 10
while i <= 30:
    new = age + i
    print(f"In {i} years, you'll be {new} years old.")
    i += 10