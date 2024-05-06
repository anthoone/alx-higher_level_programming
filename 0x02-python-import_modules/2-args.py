#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    dote = ['.', ':']
    if a == 1:
        dote = dote[0]
    elif a >= 2:
        dote = dote[1]
    if a == 1 or a > 2: 
        s = 's'
    elif a == 2:
        try:
            del s
        except NameError:
            pass
    print("{} argument{}{}".format(a-1, s if 's' in locals() else '', dote))
    
    for index, item in enumerate(sys.argv[1:]):
        print("{}: {}".format(index+1, item))
