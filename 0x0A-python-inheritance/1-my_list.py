#!/usr/bin/python3
"""
Module creates child class with
method for sorting.
"""


class MyList(list):
    """
    Class MyList inherits from list.
    """
    def __init__(self):
        super().__init__()


    def print_sorted(self):
        """
        Instance method sorts list.

        Args:
            instance: list of integers.

        Returns:
            new list sorted in ascending order.
        """

        print(sorted(self))
