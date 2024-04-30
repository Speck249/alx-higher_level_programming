#!/usr/bin/python3
"""
Module initializes new class and validates
attribute value.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size=0):
        """
        Constructor method initializes class
        with private attribute.

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
