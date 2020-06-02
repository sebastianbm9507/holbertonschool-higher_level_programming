#!/usr/bin/python3
"""
    Module that creates a function
"""


def is_same_class(obj, a_class):
    """Function that validate if a obj belong to a_class

    Arguments:
        obj  - Object to be compared
        a_class - Class to compare

    Returns:
        False or True
    """
    return type(obj) == a_class
