#!/usr/bin/python3
"""
Module implements function that
prints file contents to stdout.
"""


def read_file(filename=""):
    """
    Function opens a file, reads its content
    and prints content to console.

    Args:
        Filename: file to be read.

    Returns:
        prints output to console.
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        file_content = file.read()
        print(file_content)
