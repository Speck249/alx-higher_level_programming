#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i < len(str):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print(chr(ord(str[i]) - 32), end='')
            i += 1
        else:
            print(str[i], end='')
            i += 1
    print()
