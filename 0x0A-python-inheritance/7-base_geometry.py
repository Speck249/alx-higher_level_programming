#!/usr/bin/python3
"""
Module defines instance methods.
"""


class BaseGeometry:
    """
    Creates new class.
    """

    def area(self):
        """
        Instance method raises an exception.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Instance method validates value.

        Args:
            name: name
            value: to be validated

        Raises:
            TypeError: value must be an integer
            ValueError: value must be non-zero positive int.
        """

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
