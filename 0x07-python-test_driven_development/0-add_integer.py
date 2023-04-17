#!/usr/bin/python3
"""Module presents function that returns sum of two integers."""

def add_integer(a, b=98):
    """Function Computes sum.

    Args:
        a: first parameter
        b: second parameter

    Returns:
        Sum of two integers.

    Raises:
        TypeError: if args are not integers or floats.

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance (b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
