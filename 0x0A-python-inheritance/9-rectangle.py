#!/usr/bin/python3
"""
Module implements parent instance
methods for subclass.
"""

BaseGeometry = __import__('8-rectangle').BaseGeometry


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
            width: width of the rectangle.
            height: height of the rectangle.

        Raises:
            TypeError: width must be positive int.
            TypeError: height must be positive int.
        """

        self.__width = width
        self.integer_validator('width', width)

        self.__height = height
        self.integer_validator('height', height)

    def area(self):
        """
        Instance method returns area of rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Instance method returns string representation.
        """
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
