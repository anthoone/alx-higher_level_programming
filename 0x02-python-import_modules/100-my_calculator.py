#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    arg = sys.argv
    size = len(arg) - 1

    operators = ['+', '-', '*', '/']

    if size != 3:
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        exit(1)

    if arg[2] in operators:
        a = int(arg[1])
        b = int(arg[3])
        operator = arg[2]

        if operator == '+':
            action = add
        elif operator == '-':
            action = sub
        elif operator == '*':
            action = mul
        elif operator == '/':
            action = div
        print("{} {} {} = {}".format(a, operator, b, action(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

    exit(0)