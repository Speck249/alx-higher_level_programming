#!/usr/bin/python3
"""
Module creates subclass Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Creates new subclass that inherits
    from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Constructor method initializes class
        with private attributes.

        Args:
            width: width of rectangle.
            height: height of rectangle.

        Raises:
            TypeError: if width is not a positive int.
            TypeError: if height is not a positive int.
        """

        self.__width = width
        self.integer_validator('width', width)

        self.__height = height
        self.integer_validator('height', height)
