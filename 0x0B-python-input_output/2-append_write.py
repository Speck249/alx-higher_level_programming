#!/usr/bin/python3 
"""Module presents function that appends to file."""


def append_write(filename="", text=""):
    """Function appends to file.

    Args:
        filename: to be appended to.
        text: to be appended to file.

    Returns:
        length of text.
    """    

    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))

    f.close()
