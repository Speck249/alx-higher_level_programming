#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    val_1 = [item for item in set_1 if item not in set_2]
    val_2 = [item for item in set_2 if item not in set_1]
    return val_1 + val_2
