#!/usr/bin/python3
"""Module returns area and perimeter of rectangle."""


class Rectangle:
    """Creates new class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method instantiates new class.

        Args:
            width: first parameter
            height: second paramter
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        if self.width == 0 and self.height == 0:
            return 0

        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Method prints rectangle."""

        empty_string = ""

        if self.width == 0 and self.height == 0:
            return empty_string

        else:
            return '\n'.join(str(self.print_symbol) *
                             self.width for _ in range(self.height))

    def __repr__(self):
        """Method returns string representation of rectangle."""

        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Method deletes instance of rectangle."""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method returns biggest rectangle
        based on area.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method defines new class instance."""

        return cls(size, size)
