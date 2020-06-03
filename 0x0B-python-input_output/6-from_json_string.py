#!/usr/bin/python3
"""
Module that creates from_json_string function
"""

import json


def from_json_string(my_str):
    """Function that load a string

    Args:
        my_str (str): parameter

    Returns:
       JSON: json string
    """
    return (json.loads(my_str))
