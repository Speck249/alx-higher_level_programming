#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        sorted_list = sorted(my_list)
        max_num = sorted_list[0]
        for num in sorted_list:
            if num > max_num:
                max_num = num
        return max_num
    else:
        None
