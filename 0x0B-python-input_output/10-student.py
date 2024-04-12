#!/usr/bin/python3
"""
Module returns class attributes.
"""


class Student:
    """
    Creates new class.
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor method initializes class
        with public attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Instance method accepts list of attributes. After
        type validation, if attributes belong to class,
        method returns attribute-value pair in dictionary
        format. Otherwise, instance attribute dictionary
        is returned.
        """

        all_attributes = self.__dict__.copy()

        if type(attrs) is not list:
            return all_attributes

        for attr in attrs:
            if type(attr) is not str:
                return all_attributes

        return {attr: all_attributes[attr] for attr
                in attrs if attr in all_attributes}
