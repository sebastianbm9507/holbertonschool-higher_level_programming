#!/usr/bin/python3
import json
"""
Module that creates to_json_string
"""


def to_json_string(my_obj):
    """
    Function that convert an object to JSON string

    Args:
        my_obj (obj): Object to be converted to string

    Returns:
        String: My obj converted to string
    """
    jsonStr = json.dumps(my_obj)
    return (jsonStr)
