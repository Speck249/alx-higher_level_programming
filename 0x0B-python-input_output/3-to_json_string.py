#!/usr/bin/python3
"""
Module implements function that
serializes Python object.
"""

import json


def to_json_string(my_obj):
    """
    Function accepts Python object, and
    returns its string representation in
    JSON format.

    Args:
        my_obj: Python object.

    Returns:
        JSON string.
    """

    return json.dumps(my_obj)
