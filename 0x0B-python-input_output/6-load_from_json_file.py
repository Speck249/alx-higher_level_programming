#!/usr/bin/python3
"""
Module implements function that deserializes
JSON string from a file.
"""

import json


def load_from_json_file(filename):
    """
    Function accepts file containing JSON
    string, deconstructs and returns the
    original Python object.

    Args:
        filename: JSON file.

    Returns:
        Python object.
    """

    with open(filename, 'r', encoding='UTF-8') as file:
        return json.load(file)
