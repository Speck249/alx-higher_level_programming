#!/usr/bin/python3
"""Module prevents instance instantiation."""


class LockedClass:
    """Creates empty class."""

    __slots__ = ['first_name']
