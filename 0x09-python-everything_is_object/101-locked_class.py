#!/usr/bin/python3
"""
Module prevents dynamic instance
attribute creation.
"""


class LockedClass:
    """
    Explicity defines a fixed set of instance
    attributes at class level. Any attribute not
    listed in slots will raise an AttributeError. 
    """

    __slots__ = ['first_name']
