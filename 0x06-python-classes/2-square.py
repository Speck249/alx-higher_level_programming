#!/usr/bin/python3
"""
Module creates new class with private
attribute and enforces error checking.
"""


class Square:
    """
    Creates an empty class.
    """

    def __init__(self, size=0):
        """
        Constructor method instantiates new class.

        Args:
          size: size of the square.

        Raises:
          TypeError: size must be an integer.
          ValueError: size must be positive integer
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
