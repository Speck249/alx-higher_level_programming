#!/usr/bin/python3
"""Module returns dictionary representation."""


class Student:
    """Creates empty class."""

    def __init__(self, first_name, last_name, age):
        """Instantiates class."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation."""

        return (self.__dict__)
