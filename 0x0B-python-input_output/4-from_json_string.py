#!/usr/bin/python3
"""
Module implements function that
deserializes JSON string.
"""

import json


def from_json_string(my_str):
    """
    Function accepts JSON string, deconstructs
    and returns original Python object.

    Args:
        my_str: JSON string

    Returns:
        Python object
    """

    return json.loads(my_str)
