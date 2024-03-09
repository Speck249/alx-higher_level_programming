#!/usr/bin/python3
"""
Module defines a new class,
with private attributes.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size):
        """
        Constructor method initializes class
        with private attributes.

        Args:
          size: size of the square.
        """

        self.__size = size
