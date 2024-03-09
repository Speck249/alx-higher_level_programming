#!/usr/bin/python3
"""
Module accesses and modifies value
of private attribute.
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
        """

        self.__size = size

    @property
    def size(self):
        """
        Getter method retrieves size of square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method modifies value of square size.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Instance method calculates area of square.

        Returns:
          area of square.
        """

        return self.__size ** 2
