#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = []

    for i in a_dictionary:
        if a_dictionary[i] == value:
            new_dict.append(i)

    for j in new_dict:
        del a_dictionary[j]
    return a_dictionary
