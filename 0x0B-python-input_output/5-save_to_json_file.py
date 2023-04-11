#!/usr/bin/python3
"""Module presents function that writes Object to file."""
import json


def save_to_json_file(my_obj, filename):
    """Function writes Object to file, using JSON.

    Args:
        my_obj: to be written into file.
        filename: to be written into.

    Raises:
        TypeError: wrong object format.
    """

    json_obj = json.dumps(my_obj)
    with open(filename, 'w', encoding= "utf-8") as f:
        f.write(json_obj)

    f.close()
