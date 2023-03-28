#!/usr/bin/python3
"""Python Classes & Objects."""


class Square:
    """Creates a class."""

    def __init__(self, size=0):
        """Instantiates new class.
        Args:
            size: size of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if value of size is negative.
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

