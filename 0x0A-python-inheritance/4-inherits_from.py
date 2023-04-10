#!/usr/bin/python3
"""Module presents function that checks instance."""


def inherits_from(obj, a_class):
    """Function checks if object is instance
    of a subclass.
 
    Args:
        obj: first parameter
        a_class: second parameter

    Returns:
        returns Boolean value.

    Raises:
        no exceptions are raise.
    """

    if issubclass(a_class, (obj, a_class)):
        return True
    else:
        return False
