#!/usr/bin/python3

def common_elements(set_1, set_2):
    n = len(set_1)
    m = len(set_2)
    if n > 0 and m > 0:
        result = [i for i in set_1 if i in set_2]
        return result
