#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upp = char
        if ord(char) >= 97 and ord(char) <= 122:
            upp = chr(ord(char) - 32)
        print("{}".format(upp), end='')
    print()
