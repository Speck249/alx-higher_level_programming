#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        ld = abs(number) % 10
        print("{:d}".format(ld), end="")
        return ld
    else:
        ld = number % -10
        ld = ld * -1
        print("{:d}".format(ld), end="")
        return ld
