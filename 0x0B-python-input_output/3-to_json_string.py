#!/usr/bin/python3
"""
Module implements function that
serializes Python object.
"""

import json


def to_json_string(my_obj):
    """
    Function takes in Python object, converts
    it into its string representation in JSON
    format and returns output.

    Args:
        my_obj: Python object.

    Returns:
        string representation of object.
    """

    return json.dumps(my_obj)
