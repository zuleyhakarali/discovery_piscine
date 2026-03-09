#!/usr/bin/env python3

def array_of_names(p):
    names = []
    for first, last in p.items():
        comb = first.capitalize() + " " + last.capitalize()
        names.append(comb)
    return names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))