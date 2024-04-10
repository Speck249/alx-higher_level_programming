#!/usr/bin/python3
"""
Module implements function that
checks for instance.
"""


def is_kind_of_class(obj, a_class):
    """
    Function validates object as
    instance of class or subclass.

    Args:
        obj: class instance
        a_class: class.

    Returns:
        Boolean value.
    """

    return isinstance(obj, a_class)
