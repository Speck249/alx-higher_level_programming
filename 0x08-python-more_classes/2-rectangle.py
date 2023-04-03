#!/usr/bin/python3
"""Module instantiates new class."""


class Rectangle:
    """Creates a class."""

    def __init__(self, width=0, height=0):
        """Instantiates the new class.
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        Raises:
            TypeError: if width and height are not an integer.
            ValueError: if width and height are less than 0.
        """
        self.__width= width
        self.__height = height

    @property
    def width(self):
        """Method retrieves width of rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Method sets width of rectangle."""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Method retrieves height of rectangle"""

        return self.__height

    @width.setter
    def height(self, value):
        """Method sets height of rectangle."""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculate area of the rectangle.
        Returns: area of the rectangle.
        """

        result = self.__width * size.__height
        return result

    def perimeter(self):
       """
       Calculate perimeter of the rectangle.
       Returns: perimeter of the rectangle.
       """
       
       if width > 0 and height > 0:
           output = 2 * (self.__width + self.__height)
           return output
