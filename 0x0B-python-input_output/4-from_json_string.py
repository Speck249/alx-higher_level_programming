#!/usr/bin/python3
"""Module presents function that returns Python object."""
import json


def from_json_string(my_str):
    """Function returns Python object.

    Args:
        my_str: parameter.

    Returns:
        Python data structures.
    """

    json_obj = json.loads(my_str)
    return json_obj
