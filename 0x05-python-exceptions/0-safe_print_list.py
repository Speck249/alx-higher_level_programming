#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for ls in range(x):
        try:
            print("{}".format(my_list[ls]), end="")
            i += 1
        except IndexError:
            break
    print()
    return i
