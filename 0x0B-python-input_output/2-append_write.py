#!/usr/bin/python3
"""
Module implements function
that appends into file.
"""


def append_write(filename="", text=""):
    """
    Function opens file, appends content
    then returns count of appended chars.

    Args:
       filename: to be appended into.
       text: content appended into file.

    Returns:
       length of characters appended.
    """

    with open(filename, 'a', encoding='UTF-8') as file:
        append_content = file.write(text)
        return append_content
