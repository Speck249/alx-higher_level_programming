#!/usr/bin/python3
"""Module inherits from Base Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from Base Geometry."""

    def __init__(self, width, height):
        """Method instantiates class."""

        self.__width = width
        self.integer_validator("width", width)
        """validates value of width."""

        self.__height = height
        self.integer_validator("height", height)
        """validates value of height."""

    def area(self):
        """Computes area of rectanlge.
        Returns: area of rectangle
        """

        result = self.__width * self.__height
        return result

    def __str__(self):
        """Dunder method returns string representation."""

        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
