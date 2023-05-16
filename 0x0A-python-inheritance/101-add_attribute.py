#!/usr/bin/python3
"""Module assigns new attribute to object."""


def add_attribute(my_obj, name, value):
    """Method sets new attribute to object
    if attribute doesn't already exist.

    Args:
        my_obj: to be assigned an attribute
        name: attribute name
        value: attribute value

    Raises:
        TypeError: for exisitng attribute
    """

    if not hasattr(my_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(my_obj, name, value)
