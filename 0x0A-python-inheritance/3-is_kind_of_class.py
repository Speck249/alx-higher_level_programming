#!/usr/bin/python3
"""Module presents function that checks for subclass."""


def is_kind_of_class(obj, a_class):
    """Function checks whether object is instance
    of a class and inherited class.

    Args:
        obj: first parameter
        a_class: second parameter

    Returns:
        Boolean value.

    Raises:
        no exceptions are raised.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
