#!/usr/bin/python3
"""Module returns dictionary representation."""


class Student:
    """Creates empty class."""

    def __init__(self, first_name, last_name, age):
        """Instantiates class."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation."""

        all_attr = self.__dict__.copy()

        if type(attrs) is list:
            for a in attrs:
                if type(a) is not str:
                    return all_attr

            attr_dict = {}

            for i in range(len(attrs)):
                for j in all_attr:
                    if attrs[i] == j:
                        attr_dict[j] = all_attr[j]

            return attr_dict

        else:
            return all_attr 

