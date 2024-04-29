#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    unique_val = set(my_list)
    for val in unique_val:
        total += val
    return total
