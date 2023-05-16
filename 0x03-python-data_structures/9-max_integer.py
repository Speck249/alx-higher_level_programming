#!/usr/bin/python3

def max_integer(my_list=[]):
    n = len(my_list)

    if n == 0:
        return (None)

    max_num = my_list[0]

    if n > 0:
        for x in my_list[1:]:
            if x > max_num:
                max_num = x
        return max_num
