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
        Constructor method initializes class
        with private attribute.

        Args:
            size: size of the square.
            position: location of square along coordinate.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method retrieves size of square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method modifies size of square.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        Getter method retrieves position of square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method modifies position of square.
        """

        if (
                len(value) != 2 or
                not isinstance(value, tuple) or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Instance method Calculate area of square.

        Returns:
          area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Instance method prints square along x, y coordinate.
        """

        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print('')
        for row in range(self.__size):
            if self.__position[0] > 0:
                print('#' * self.__position[0], end='')
            for col in range(self.__size):
                print('#', end='')
            print()
