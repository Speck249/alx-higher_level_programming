#!/usr/bin/python3
"""
Module executes operator overloading.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size=0):
        """
        Constructor method initializes new class
        with private attribute.

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

        Args:
          value: new value for square size.

        Raises:
          TypeError: size must be an integer or float.
          ValueError: size must be positive integer or float.
        """

        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Instance method calculates area of square.

        Returns:
          area of the square.
        """

        return self.__size ** 2

    def __eq__(self, other):
        """
        Instance method evaluates equality of instance
        values.

        Args:
          self: accesses instance attribute value.
          other: signifies to operator that instance
                 represents second operand.

        Returns:
          True if instance values are equal, False otherwise.
        """

        return self.__size == other.__size

    def __ne__(self, other):
        """
        Instance method evaluates equality of instance
        values.

        Args:
          self: accesses instance attribute value.
          other: signifies to operator that instance
                 represents second operand.

        Returns:
          True if instance values are not equal, False otherwise.
        """

        return self.__size != other.__size

    def __gt__(self, other):
        """
        Instance method evaluates instance values.

        Args:
          self: accesses instance attribute value.
          other: signifies to operator that instance
                 represents second operand.

        Returns:
          True if first instance value is greater than
          second instance value, False otherwise.
        """

        return self.__size > other.__size

    def __ge__(self, other):
        """
        Instance method evaluates instance values.

        Args:
          self: accesses instance attribute value.
          other: signifies to operator that instance
                 represents second operand.

        Returns:
          True if first instance value is greater than
          or equal to second instance value, False otherwise.
        """

        return self.__size >= other.__size

    def __lt__(self, other):
        """
        Instance method evaluates instance values.

        Args:
          self: accesses instance attribute value.
          other: signifies to operator that instance
                 represents second operand.

        Returns:
          True if first instance value is less than
          second instance value, False otherwise.
        """

        return self.__size < other.__size

    def __le__(self, other):
        """
        Instance method evaluates instance values.

        Args:
          self: accesses instance attribute value.
          other: signifies to operator that instance
                 represents second operand.

        Returns:
          True if first instance value is less than or
          equal to second instance value, False otherwise.
        """

        return self.__size <= other.__size
