#!/usr/bin/python3
"""Python Classes and Objects."""

class Square:
    """Creates en empty class Square which defines a square."""

    def __init__(self, size=0):
        """The init method instantiates the empty class
        with a new object.
        Args:
            size = size of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if the value of size is negative.
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Computes the area of the square.
        Prints result.
        """

        result = self.__size ** 2
        return result
