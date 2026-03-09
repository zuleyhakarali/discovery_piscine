#!/usr/bin/env python3

print("Enter the first number:")
fir = int(input())
print("Enter the second number:")
sec = int(input())

output = fir * sec
print(f"{fir} x {sec} = {output}")
if output == 0:
    print("The result is positive and negative.")
elif output > 0:
    print("The result is positive.")
elif output < 0:
    print("The result is negative.")
