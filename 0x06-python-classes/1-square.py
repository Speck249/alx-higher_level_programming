#!/usr/bin/python3
"""
Module defines a new class, with private
attribute.
"""


class Square:
    """
    Creates new class.
    """

    def __init__(self, size):
        """
        Constructor method initializes class
        with private attribute.

        Args:
          size: size of the square.
        """

        self.__size = size
