#!/usr/bin/python3
if __name__ == "__main__":   
    import sys
    i = len(sys.argv) - 1
    if i == 0 and i == 1:
        print("{} arguments.".format(i))

    elif i > 0:
        print("{} arguments:".format(i))
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i = i + 1
