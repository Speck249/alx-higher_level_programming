#!/usr/bin/python3
"""Module returns area and perimeter of rectangle."""


class Rectangle:
    """Creates new class"""

    def __init__(self, width=0, height=0):
        """Method instantiates new class.

        Args:
            width: first parameter
            height: second paramter
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Method retrieves width.

        Returns:
            value of width.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Method sets value of width.

        Args:
            value: parameter

        Raises:
            TypeError: if width is not int.
            ValueError: if width < 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method retrieves height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Method sets height value.

        Args:
            value: parameter

        Raises:
            TypeError: if height is not int.
            ValueError: if height < 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method computes area of rectangle.
        Returns: area of rectangle.
        """

        return self.width * self.height

    def perimeter(self):
        """Method computes perimeter of rectangle.
        Returns: perimeter of rectangle.
        """

        if self.width == 0 or self.height == 0:
            return 0

        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Method prints rectangle."""

        empty_string = ""

        if self.width == 0 or self.height == 0:
            return empty_string
        else:
            return ('\n'.join("#" * self.width for _ in range(self.height)))
