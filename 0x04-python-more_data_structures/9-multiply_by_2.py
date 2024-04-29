#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in sorted(a_dictionary.items())}
