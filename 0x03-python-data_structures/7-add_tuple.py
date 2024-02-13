#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_a) == 1:
        output_one = tuple_a[0] + tuple_b[0]
        output_two = 0 + tuple_b[1]
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_b) == 1:
        output_one = tuple_a[0] + tuple_b[0]
        output_two = tuple_a[1] + 0
    else:
        output_one = tuple_a[0] + tuple_b[0]
        output_two = tuple_a[1] + tuple_b[1]

    result = (output_one, output_two)
    return result
