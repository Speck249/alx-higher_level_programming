#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ''
    for idx in range(0, len(str)):
        if idx != n:
            new_str += str[idx]
    return new_str
