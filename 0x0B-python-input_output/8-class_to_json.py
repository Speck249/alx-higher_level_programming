#!/usr/bin/python3
"""Module returns dictionary description."""


def class_to_json(obj):
    """Function returns dictionary description
    for JSON serialization of an object.
    """

    return (obj.__dict__)
