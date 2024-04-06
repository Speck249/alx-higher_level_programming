#!/usr/bin/python3
"""
Module implements function that
prints string.
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

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')
