#!/usr/bin/python3
"""Module presents method that validates value."""


class BaseGeometry:
    """Creates an empty class."""

    def area(self):
        """Class method not implemented."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates value.

        Args:
            name: name of value
            value: to be validated
 
        Returns:
            no return value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
