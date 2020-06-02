#!/usr/bin/python3
"""
    Module that creates a function to identify the instance on an object
"""


def is_kind_of_class(obj, a_class):
    """
    Identify the instance of an object

    Arguments:
        obj
        a_class

    Returns:
        True, is instance, False, no is instance
    """
    return isinstance(obj, a_class)
