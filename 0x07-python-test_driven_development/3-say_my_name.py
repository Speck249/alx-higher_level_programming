#!/usr/bin/python3
"""Module presents function that prints first and last name."""

def say_my_name(first_name, last_name=""):
    """Returns first and last name.

    Args:
        first_name: first parameter
        last_name: second parameter

    Returns:
        Prints first and last name to console.

   Raises:
        TypeError: if args are not strings.

   """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
