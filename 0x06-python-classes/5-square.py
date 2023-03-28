#!/usr/bin/python3
"""Python Classes & Objects."""


class Square:
    """Creates a class."""

    def __init__(self, size=0):
        """Instantiates the new class.
        Args:
            size: size of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if value of size is negative.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square."""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square from given size.
        Returns: area of the square.
        """

        result = self.__size ** 2
        return result

    def my_print(self):
        """Method prints a square."""
        
        if not self.__size:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
