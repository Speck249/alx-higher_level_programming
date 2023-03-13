#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return (None)

    n = len(my_list)

    if idx >= n:
        return (None)

    else:
        return my_list[idx]
