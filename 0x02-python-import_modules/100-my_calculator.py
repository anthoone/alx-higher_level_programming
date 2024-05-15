#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg = sys.argv
    size = len(arg) - 1

    operators = ['+', '-', '*', '/']

    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
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
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        print("{} {} {} = {}".format(a, operator, b, action(a, b)))
        exit(0)