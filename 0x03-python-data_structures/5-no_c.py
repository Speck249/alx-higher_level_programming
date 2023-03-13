#!/usr/bin/python3

def no_c(my_string):
    new_string = my_string[:]
    bad_char = ["c", "C"]
    new_string = ''.join((filter(lambda i: i not in bad_char,
    new_string)))
    return new_string
