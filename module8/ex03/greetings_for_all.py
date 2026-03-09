#!/usr/bin/env python3

import sys

def greetings(name=None):
    if name is None:
        name = "noble stranger"
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)