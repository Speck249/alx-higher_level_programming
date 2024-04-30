#!/usr/bin/python3
"""
Module initializes new class and defines instance
methods.
"""


class Rectangle:
    """
    Creates new class and public class attributes.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor method initializes new class
        with private attributes and increments
        instance count.

        Args:
            width: width of rectangle.
            height: height of rectangle.
        """

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Dunder method returns human readable string
        representation of class instance.
        """

        res = ''
        symbol = str(self.print_symbol)
        if self.__width != 0 and self.__height != 0:
            for row in range(self.__height):
                if row < self.__height - 1:
                    print(symbol * self.__width)
                if row == self.__height - 1:
                    print(symbol * self.__width, end='')
        return f'{res}'

    def __repr__(self):
        """
        Dunder method returns string representation for
        class instance recreation or debugging.
        """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """
        Destructor method executes cleanup before object
        is removed from memory following deletion.
        """

        print(f'Bye rectangle...')
        Rectangle.number_of_instances -= 1

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

        Args:
            value: new value for rectangle width.

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
        Getter method retrieves height of rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Instance method modifies value of height.

        Args:
            value: new value for rectangle height.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be positive integer.
        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Instance method computes area of rectangle.

        Returns:
          area of rectangle.
        """

        return self.width * self.height

    def perimeter(self):
        """
        Instance method computes perimeter of rectangle.

        Returns:
          perimeter of rectangle.
        """

        if self.width == 0 and self.height == 0:
            return 0
        return 2 * (self.width + self.height)
