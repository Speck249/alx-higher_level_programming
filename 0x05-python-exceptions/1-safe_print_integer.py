#!/usr/bin/python3 

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        result = isinstance(value, int)
        if result == True:
            return True
    except ValueError:
        return False
