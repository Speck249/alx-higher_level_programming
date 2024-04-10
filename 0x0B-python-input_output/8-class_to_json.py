#!/usr/bin/python3
"""
Module implements function that
returns dictionary description.
"""


def class_to_json(obj):
    """
    Function accepts class instance, 
    converts object attributes to
    dictionary format in preparation
    for JSON serialization.
    """

    return (obj.__dict__)
