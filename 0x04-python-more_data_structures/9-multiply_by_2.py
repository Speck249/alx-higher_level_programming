#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copy_of_a_dictionary = a_dictionary.copy()
    for key, value in copy_of_a_dictionary.items():
        copy_of_a_dictionary[key] = value * 2
    return copy_of_a_dictionary
