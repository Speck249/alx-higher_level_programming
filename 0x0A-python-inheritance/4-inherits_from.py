#!/usr/bin/python3
"""Module presents function that checks instance."""


def inherits_from(obj, a_class):
    """Function checks if object is instance
    of a subclass.
 
    Args:
        obj: instance
        a_class: subclass

    Returns:
        returns parent class if True.

    """

    if type(obj) is a_class:
        return False
 
    return isinstance(obj, a_class)
