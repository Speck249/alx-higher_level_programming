#!/usr/bin/python3
"""Python Classes & Objects."""


class Square:
    """Creates a class."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiates the new class.
        Args:
            size: size of the square.
            position: coordinate of the square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Method retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Method sets size of square."""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Method retrieves position of square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Method sets position of square."""

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate area of the square from given size.
        Returns: area of the square.
        """

        result = self.__size ** 2
        return result

    def my_print(self):
        """Method prints square."""

        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print()i
        for i in range(0, self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for k in range(self.size):
                print("#", end="")
            print()
