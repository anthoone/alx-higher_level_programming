#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M" : 1000
    }
    N = len(roman_string)
    i = N - 1
    sum = 0
    while i >= 0:
        if i < N - 1 and lookup[roman_string[i]] < lookup[roman_string[i + 1]]:
            sum -= lookup[roman_string[i]]
        else:
            sum += lookup[roman_string[i]]
        i -= 1
    return (sum)