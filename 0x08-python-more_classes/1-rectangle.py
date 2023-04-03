#!/usr/bin/python3
"""Module instantiates class."""


class Rectangle:
    """Creates a class."""

    def __init__(self, width=0, height=0):
    """Instantiates the new class.
    Args:
        width - width of rectangle.
        height - height of rectangle.
    Raises:
        TypeError: if width or height are not integers.
        ValueError: if width or height are less than zero.
    """

    self.width = width
    self.height = height
    
    @property
    def width(self):
        """Method retrieves width of rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Method sets width of rectangle."""
    
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method retrieves height of rectangle."""
    
        return self.__height
    
    @height.setter
    def height(self, value):
        """Method sets height of rectangle."""
    
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
