#!/usr/bin/python3
"""
Shallow copies are affected by modifications
in the event of nesting
"""
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return new_list
    else:
        new_list[idx] = element
        return new_list
