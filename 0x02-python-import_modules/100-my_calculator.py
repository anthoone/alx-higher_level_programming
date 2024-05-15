#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg = sys.argv
    size = len(arg) - 1

    operators = ['+', '-', '*', '/']

    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    else:
        a = int(arg[1])
        b = int(arg[3])
        operator = arg[2]

        for i in operators:
            if operator != i:
                print("Unknown operator. Available operators: +, -, * and /\n")
                exit(1)
            else:
                print("{} {} {} = {}".format(a, operator, b, add(a, b)))
                exit(0)