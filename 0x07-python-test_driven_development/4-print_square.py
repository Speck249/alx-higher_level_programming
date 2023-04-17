#!/usr/bin/python3
"""Module presents function that prints a square."""

def print_square(size):
    """Prints a square to console.

    Args:
        size - length of the square.

    Returns:
        no return value

    Raises:
        TypeError: if size is not an int and less than 0.
        ValueError: if size is less than 0.

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print("")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
