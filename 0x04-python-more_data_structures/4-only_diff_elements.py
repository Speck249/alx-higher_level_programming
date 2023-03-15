#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    n = len(set_1)
    m = len(set_2)
    if n > 0 and m > 0:
        result = [i for i in set_1 if i not in set_2] + [j for j in set_2 if j not in set_1]
        return result
