#!/usr/bin/python3
"""
Module inverts normal operation
of integer class methods.
"""


class MyInt(int):
    """
    Creates new subclass.
    """

    def __eq__(self, other):
        """
        Instance method checks for inequality.

        Args:
            self: accesses instance attribute value.
            other: signifies to operator instance
                   represents second operand.

        Returns:
            True if integer operands are not equal.
        """

        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        Instance method checks for equality.

        Args:
            self: accesses instance attribute value.
            other: signifies to operator instance
                   represents second operand.

        Returns:
            True if integer operands are equal.
        """

        return int.__eq__(self, other)
