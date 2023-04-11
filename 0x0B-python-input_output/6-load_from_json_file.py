#!/usr/bin/python3
"""Module presents function that creates object."""
import json


def load_from_json_file(filename):
    """Function creates object from JSON file.

    Args:
        filename: JSON file
    """

    with open(filename, 'r') as f:
        return json.load(f)

    f.close()
