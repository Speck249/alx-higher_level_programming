#!/usr/bin/python3
"""Module presents sorting method."""

class MyList(list):
    """Creates child class."""

    def print_sorted(self):
        """Methods sorts list.

        Returns:
            sorted list.
        """

        result = sorted(self)
        print(result)
