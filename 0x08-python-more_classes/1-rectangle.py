#!/usr/bin/python3
"""Module creates class."""


class Rectangle:
    """Creates class."""

    def __init__(self, height=0, width=0):
    """Instantiates new class.
    Args:
        width - width of rectangle.
        height - height of rectangle.
    """

    self.__height = height
    self.__width = width
    
    @property
    def width(self):
    """Retrieves width of rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
    """Sets width of rectangle."""
    
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
    """Retrieves height of rectangle."""
    
        return self.__height
    
    @height.setter
    def height(self, value):
    """Sets width of rectangle."""
    
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
