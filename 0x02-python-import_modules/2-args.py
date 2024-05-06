#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    dote = ['.', ':']
    if a == 1:
        dote = dote[0]
    elif a >= 2:
        dote = dote[1]

    print("{} arguments{}".format(a-1, dote))

    for index, item in enumerate(sys.argv[1:]):
        print("{}: {}".format(index+1, item))
