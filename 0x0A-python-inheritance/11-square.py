#!/usr/bin/python3
"""
Module creates subclass of Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creates a new subclass that inherits
    from Rectangle.
    """
    def __init__(self, size):
        """
        Constructor method initializes class
        with private attribute.

        Arg:
           size: size of the square.

        Raises:
            TypeError: size must be positive int.
        """

        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        """
        Instance method returns string representation.
        """
        return f'[{self.__class__.__name__}] {self.__size}/{self.__size}'
