#!/usr/bin/python3
"""Module presents function that appends into file."""


def append_write(filename="", text=""):
    """Function appends into file.

    Args:
       filename: to be appended into.
       text: to be appended into file.

    Returns:
       length of text.
       appended text content.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

    f.close()
