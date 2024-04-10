#!/usr/bin/python3
"""
Module implements function that
checks for instance.
"""


def inherits_from(obj, a_class):
    """
    Function validates object as
    instance of subclass.

    Args:
        obj: class instance
        a_class: class.

    Returns:
        Boolean value.
    """

    return issubclass(type(obj), a_class) and (type(obj) != a_class)
