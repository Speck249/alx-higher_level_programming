#!/usr/bin/python3
"""Module inherits from Rectanlge."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherits from Rectangle."""

    def __init__(self, size):
        """Method instantiates class."""

        self.integer_validator("size", size)
        """Validates value of size."""

        super().__init__(size, size)
        self.__size = size
        """Sets private class instance."""

    def area(self):
        """Computes area of square.
        Returns area of square.
        """

        return super().area()

    def __str__(self):
        """Returns square description."""

        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
