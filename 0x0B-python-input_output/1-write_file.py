#!/usr/bin/python3
"""Module presents function that writes into file."""


def write_file(filename="", text=""):
    """Function writes into file.

    Args:
       filename: to be written into.
       text: to be written into file.

    Returns:
       length of text.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

    f.close()
