#!/usr/bin/python3
"""
Module implements function that
prints square to console.
"""


def print_square(size):
    """
    Function accepts square length
    and prints accordingly.

    Args:
        size: size/length of square.

    Raise:
        TypeError: size must be integer.
        ValueError: size must be greater than 0.

    Returns:
        Prints square to console.
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        for columns in range(size):
            print('#', end='')
        print()
