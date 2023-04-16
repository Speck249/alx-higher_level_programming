#!/usr/bin/python3
"""Module presents function for new line insetion."""


def append_after(filename="", search_string="", new_string=""):
    """Method inserts new line."""
    my_str = ""

    with open(filename, encoding="utf-8") as f:
        for text in f:
            my_str = my_str + text
            if search_string in text:
                my_str = my_str + new_string

    with open(filename, 'w', encoding="utf-8") as g:
        g.write(my_str)
