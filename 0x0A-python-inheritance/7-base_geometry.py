#!/usr/bin/python3
"""Module creates empty class."""


class BaseGeometry:
    """Creates an empty class."""

    def area(self):
        """Function raises an exception.

        Args:
            passed self to instance method.

        Returns:
            no return value.

        Raises:
            a custom exception message.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function validates value.

        Args:
            name: first parameter
            value: second parameter
 
        Returns:
            no return value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
