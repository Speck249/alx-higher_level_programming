#!/usr/bin/python3
"""
Module implements function that prints string.
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints first and last name
    to console.

    Args:
        first_name: first string argument.
        last_name: second string argument.

    Raises:
        TypeError: arguments must be string.

    Returns:
        Prints first and last name to console.
    """

    if not isinstance(first_name, str)\
            or first_name.isalpha() is False:
        raise TypeError('first_name must be a string')

    if last_name and (not isinstance(last_name, str)
                      or last_name.isalpha() is False):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
