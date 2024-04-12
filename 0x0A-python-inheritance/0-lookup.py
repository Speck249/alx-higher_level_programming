#!/usr/bin/python3
"""
Module returns attributes and methods
associated with an instance.
"""


def lookup(obj):
    """
    Function returns list of available
    attributes and methods of an object.
    """

    return list(dir(obj))
