#!/usr/bin/python3
"""Module creates class that inherits from int."""


class MyInt(int):
    """Creates class that inherits from int."""


    def __eq__(self, other):
        """Runs negation check."""
        return int.__ne__(self, other)


    def __ne__(self, other):
        """Runs negation check."""
        return int.__eq__(self, other)
