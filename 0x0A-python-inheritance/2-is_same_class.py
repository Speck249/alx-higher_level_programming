#!/usr/bin/python3
"""Module presents function that checks for class."""


def is_same_class(obj, a_class):
    """Function checks whether an object is
    an exact instance of a class.

    Args:
        obj: first parameter
        a_class: second parameter

    Returns:
        Boolean value.

    Raises:
        no exceptions are raised.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
