#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    size = len(arg) - 1
    dote = ['.', ':']
    if size == 0:
        dote = dote[0]
    elif size >= 1:
        dote = dote[1]
    if size == 0 or size >= 2: 
        s = 's'
    elif size == 1:
        try:
            del s
        except NameError:
            pass
    print("{} argument{}{}".format(size, s if 's' in locals() else '', dote))
 
    for i in range(1, size + 1):
        print("{}: {}".format(i, arg[i]))
