#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            new_dict.append(key)

    for key in new_dict:
        del a_dictionary[key]
    return a_dictionary
