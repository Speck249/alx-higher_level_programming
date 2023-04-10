#!/usr/bin/python3
"""Module presents function which returns a list of
   object attributes and methods.
   """


def lookup(obj):
    """Function returns list of attributes & methods.

    Args:
        Object: parameter

    Returns:
        List of attributes & methods.
    """

    return (dir(obj))
