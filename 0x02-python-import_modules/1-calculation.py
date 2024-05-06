#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    list = [add, sub, mul, div]
    a = 10
    b = 5
    for i in list:
        if i == add:
            c = '+'
        elif i == sub:
            c = '-'
        elif i == mul:
            c = '*'
        elif i == div:
            c = '/'

        print("{} {} {} = {}".format(a, c, b, i(a, b)))
