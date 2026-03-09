#!/usr/bin/env python3

def find_the_redheads(fam):
    def is_red(name):
        return fam[name] == "red"
    new = filter(is_red, fam.keys())
    return list(new)

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))

"""
def find_the_redheads(fam):
    new = []
    for f, l in fam.items():
        if l == "red":
            new.append(f)
    return new
"""