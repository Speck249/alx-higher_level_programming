#!/usr/bin/python3
"""Module checks for subclass inheritance."""


def inherits_from(obj, a_class):
    """Function validates subclass inheritance.

    Args:
        obj: instance of a class
        a_class: class
    """

    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
