#!/usr/bin/python3
"""
Module defines a new class, 
with private attribute.
"""


class Square:
    """
    Creates an empty class.
    """

    def __init__(self, size):
        """
        Constructor method instantiates new class
        and initializes its private attribute.
        """
        self.__size = size
