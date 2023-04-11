#!/usr/bin/python3
"""Module presents function that writes to file."""
import json


def save_to_json_file(my_obj, filename):
    """Function writes object to file, using JSON.

    Args:
        my_obj: to be written into file.
        filename: to be written into.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        json.dump(my_obj, f)

    f.close()
