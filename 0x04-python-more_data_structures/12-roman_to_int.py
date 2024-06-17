#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or type(roman_string) != str:
        return 0
    N = len(roman_string)
    i = N - 1
    roman_int = 0
    while i >= 0:
        if i < N - 1 and roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]:
            roman_int -= roman_dic[roman_string[i]]
        else:
            roman_int += roman_dic[roman_string[i]]
        i -= 1
    return roman_int
