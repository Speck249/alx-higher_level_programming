#!/usr/bin/python3
"""
Module implements function that
appends new line to file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function searches through file to find
    line containing search word then appends
    new line immediately after.
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='UTF-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
