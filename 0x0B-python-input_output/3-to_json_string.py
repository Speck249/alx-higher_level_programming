#!/usr/bin/python3
"""Module presents function that creates JSON format."""
import json


def to_json_string(my_obj):
    """Function converts object to string representation.

    Args:
        my_obj: parameter.

    Returns:
        JSON representation of object.
    """

    json_obj = json.dumps(my_obj, sort_keys=True)
    return json_obj
