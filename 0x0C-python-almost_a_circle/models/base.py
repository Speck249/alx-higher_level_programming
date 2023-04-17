#!/usr/bin/python3
"""Module presents base methods."""
import json
import os.path


class Base:
    """Creates class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method instantiates new class."""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method returns JSON string representation."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method saves JSON string representation to file."""
        length = len(list_objs)
        filename = cls.__name__ + ".json"

        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(list_objs)
            else:
                new_list = [ls.to_dictionary() for ls in list_objs]
                output = Base.to_json_string(new_list)
                f.write(output)

    @staticmethod
    def from_json_string(json_string):
        """Method returns list of JSON string representation"""

        empty_list = []
        if not json_string:
            return empty_list

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method returns instance with set attributes."""

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method returns a list of instances."""
        filename = cls.__name__ + ".json}"
        new_list = []
        new_list1 = []

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                output = f.read()
                new_list = cls.from_json_string(output)
                for ls in new_list:
                    new_list1.append(cls.create(**dictionary))

        return new_list1
