#!/usr/bin/python3
"""Module presents function that creates Object."""
import json


def load_from_json_file(filename):    
    """Function creates Object from JSON file.

    Args:
        filename: JSON file.

    Raises:
        FileNotFoundError: non-existing file.
        ValueError: wrong value.
    """

    with open(filename, 'r') as f:
        return json.load(f)

    f.close()
