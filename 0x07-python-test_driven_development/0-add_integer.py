#!/usr/bin/python3
"""
Module implements function that
returns sum of two integers.
"""


def add_integer(a, b=98):
    """
    Method executes type conversion of
    arguments, calculates and returns
    their sum.

    Args:
        a: an integer or float.
        b: an integer or float.

    Raises:
        TypeError: both operands must be integers.

    Returns:
        sum of two integers.
    """

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    else:
        a = int(a)

    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')
    else:
        b = int(b)

    return a + b
