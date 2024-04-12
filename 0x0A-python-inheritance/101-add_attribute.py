#!/usr/bin/python3
"""
Module implments function assigning
new attribute to object.
"""


def add_attribute(obj, name, value):
    """
    Method accepts instance, new attribute
    name and corresponding value. It validates
    if instance supports dynamic attribute
    assignment. Otherwise, it raises an error.

    Args:
        obj: instance of a class.
        name: new attribute name.
        value: new attribute value.

    Raises:
        TypeError: instance must support dynamic
                   attribute assignment.

    Returns:
        new attribute value.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')

    setattr(obj, name, value)
