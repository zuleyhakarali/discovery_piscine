#!/usr/bin/env python3

fir = 0
while fir < 11:
    print(f"Table of {fir}:", end="")
    sec = 0
    while sec < 11:
        num = fir * sec
        print(f" {num}", end="")
        sec += 1
    print()
    fir += 1