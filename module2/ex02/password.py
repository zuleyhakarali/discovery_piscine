#!/usr/bin/env python3

password = "Python is awesome"
check = input()
if check == password:
    print("ACCESS GRANTED")
elif check != password:
    print("ACCESS DENIED")
