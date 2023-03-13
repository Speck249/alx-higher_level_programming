#!/usr/bin/python3

def no_c(my_string):
    new_string = my_string[:]
    bad_char = ['c', 'C']
    new_string = ''.join(i for i in my_string if
    not i in bad_char)
    return new_string
