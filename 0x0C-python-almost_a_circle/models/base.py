#!/usr/bin/python3
"""
Module Initializes Superclass and defines methods.
"""

import json
import csv
import os.path


class Base:
    """
    Creates new Superclass with Private class
    attribute for counting class objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method initializes class with public attribute.

        Args:
            id: unique instance identification.

        Returns:
            Class initialization returns an id number, or
            __nb_objects when id defaults to None.
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method converts dictionary to JSON format.

        Args:
            list_dictionaries: dictionary of subclass
            attribute-value pair.

        Returns:
            JSON string representation.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method converts list of instance attribute-value
        pairs into dictionary that is serialized into JSON string
        and saved into new file.

        Args:
            cls: target subclass name.
            list_objs: list of subclass instances with 
            attribute values.
        """

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='UTF-8') as file:
            if list_objs is None:
                file.write('[]')
            else:
                dict_list = [item.to_dictionary() for item in list_objs]
                json_string = Base.to_json_string(dict_list)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method deserializes JSON string into original format.

        Args:
            json_string: list of JSON string.
        """

        if not json_string:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method recreates class instance with set attributes.

        Args:
            cls: name of target subclass.
            **dictionary: keyword attributes passed to update() method.

        Returns:
            class instances with attribue values.
        """
        
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy = cls(2)

        return dummy.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """
        Class method deserializes json string from file, and creates
        list of class instances.

        Args:
            cls: name of target subclass.

        Returns:
            List of objects.
        """
        
        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as file:
                json_content = file.read()
                first_list = cls.from_json_string(json_content)
                list_objs = []
                for item in first_list:
                    list_objs.append(cls.create(**item))
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method serializes in CSV file.

        Arg:
            cls: subclass of Base
            list_objs: list of instances
        """

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='UTF-8') as file:
            if not list_objs:
                file.write('[]')
            else:
                if cls.__name__ == 'Square':
                    fieldnames = ['id', 'size', 'x', 'y']
                elif cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for item in list_objs:
                    item_dict = item.to_dictionary()
                    for key, value in item_dict.items():
                        writer.writerow(value)

    def load_from_file_csv(cls):
        """Method deserializes csv file."""
        with open(filename, 'r', lines="") as f:
            if cls.__name__ == "Square":
                column = ['id', 'size', 'x', 'y']
            elif cls.__name__ == "Rectangle":
                column = ['id', 'width', 'height', 'x', 'y']

            res = csv.DictReader(f, column=column)
            res = [dict([key, int(value)] for key, value in i.items())
                   for i in csv_items]
            output = [cls.create(**i) for i in read_from_csv]
            return output
