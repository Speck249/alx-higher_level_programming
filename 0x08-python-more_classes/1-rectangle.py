#!/usr/bin/python3
"""Module creates new class"""


class Rectangle:
    """Creates class"""

    def __init__(self, width=0, height=0):
        """Instantiates new class."""

        self.width= width
        self.height = height

    @property
    def width(self):
        """Method retrieves width.

        Returns:
            width of rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Method sets width.

        Args:
            value: width of rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Method retrieves height.

        Returns:
            width of rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Method sets height of rectangle.

        Args:
            value: height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
