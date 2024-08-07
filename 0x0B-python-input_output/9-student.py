#!/usr/bin/python3
"""
Module creates class with method
that retrieves dictionary.
"""


class Student:
    """
    Creates new class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor method initializes class
        with public attributes.

        Args:
            first_name
            last_name
            age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary representation
        of instance attributes.
        """

        return (self.__dict__)
