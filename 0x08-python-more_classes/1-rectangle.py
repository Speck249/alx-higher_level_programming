#!/usr/bin/python3
"""
Module initializes new class with private
attributes, setter and getter methods.
"""


class Rectangle:
    """
    Creates new class.
    """

    def __init__(self, width=0, height=0):
        """
        Constructor method initializes class
        with private attributes.

        Args:
            width: width of rectangle.
            height: height of rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method retrieves width of rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method modifies value of width.

        Raises:
            TypeError: width must be an integer.
            ValueError: width must be positive integer.
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter method retrieves height of rectanlge.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method modifies value of height.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be positive integer.
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
