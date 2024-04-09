#!/usr/bin/python3
"""
Module implements function that
populates and counts file content.
"""


def write_file(filename="", text=""):
    """
    Function writes into file, counts and
    returns characters written into file.

    Args:
       filename: to be written into.
       text: indended file content.

    Returns:
       length of file content.
    """

    with open(filename, 'w', encoding='UTF=8') as file:
        content_count = file.write(text)
        return content_count
