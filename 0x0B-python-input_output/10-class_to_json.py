#!/usr/bin/python3
"""
Module
"""


def class_to_json(obj):
    """Class to json

    Args:
        obj (obj): Obj to be represented in dict mode

    Returns:
        obj: obj represented in dict
    """
    return (obj.__dict__)
