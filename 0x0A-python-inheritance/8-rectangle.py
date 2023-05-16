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
