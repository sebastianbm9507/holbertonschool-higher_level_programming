#!/usr/bin/python3
"""
Module that creates to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Function that convert an object to JSON string

    Args:
        my_obj (obj): Object to be converted to string

    Returns:
        String: My obj converted to string
    """
    return (json.dumps(my_obj))
