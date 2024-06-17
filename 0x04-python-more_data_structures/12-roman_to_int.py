#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    lookup = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    n = len(roman_string)
    total = 0
    i = 0
    
    while i < n:
        if i < n - 1 and lookup[roman_string[i]] < lookup[roman_string[i + 1]]:
            total -= lookup[roman_string[i]]
        else:
            total += lookup[roman_string[i]]
        i += 1
    return total