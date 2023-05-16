#!/usr/bin/python3

def uniq_add(my_list=[]):
    res = 0
    new_list = set(my_list)
    my_list = (list(new_list))
    for i in my_list:
        res = res + i
    return res
