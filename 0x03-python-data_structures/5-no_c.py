#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in list(my_string):
        if i == 'c' or i == 'C':
            continue
        new_string += i
    return new_string