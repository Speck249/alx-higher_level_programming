#!/usr/bin/python3
"""
Module implements function that saves
deserialized Python object in a file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function accepts Python object and
    file, converts object into JSON string
    then saves it inside target file.

    Args:
        my_obj: to be converted into JSON string.
        filename: target destination.

    Returns:
        file with JSON string.
    """

    with open(filename, 'w', encoding='UTF-8') as file:
        return json.dump(my_obj, file)
