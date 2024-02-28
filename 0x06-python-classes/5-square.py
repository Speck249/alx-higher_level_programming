#!/usr/bin/python3
"""
Module accesses and modifies value
of private attribute.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size=0):
        """
        Constructor method initializes class.

        Args:
            size: size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """
        Getter method retrieves size of square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method modifies value of square size.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Instance Method computes area of square.

        Returns:
          area of square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Instance Method prints square to stdout.
        """

        if self.__size == 0:
            print()
        for width in range(self.__size):
            for length in range(self.__size):
                print('#', end='')
            print()
