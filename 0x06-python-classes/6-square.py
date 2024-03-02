#!/usr/bin/python3
"""
Module prints square to console
along the x, y coordinate.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates new class wits private attributes.

        Args:
            size: size of the square.
            position: location of square along coordinate.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Method retrieves size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method modifies size of square.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Method retrieves position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Method modifies position of square.
        """
        if (len(value) != 2 and
                not isinstance(value, tuple) and
                not all(isinstance(num, int) for num in value) and
                all(num < 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate area of the square from given size.
        Returns: area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Method prints square along the x, y coordinate.
        """
        if self.__size == 0:
            print()

        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print('')
        for row in range(self.__size):
            if self.__position[0] > 0:
                print('{}'.format(chr(32) * self.__position[0]), end='')
            for column in range(self.__size):
                print('#', end='')
            print()
