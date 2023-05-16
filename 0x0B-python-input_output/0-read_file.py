#!/usr/bin/python3
"""Module presents function that reads file."""


def read_file(filename=""):
    """Function reads from file & prints content.

    Args:
        Filename: file to be read.

    Returns:
        no return value.
        prints output to console.
    """

    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end="")

    f.close()
