#!/usr/bin/python3
"""
Module calculates and returns
area of square.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size=0):
        """
        Constructor method initializes class
        with private attributes.

        Args:
            size: size of the square.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be positive integer.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Instance method calculates area of square.

        Returns:
          area of square.
        """

        return self.__size ** 2
