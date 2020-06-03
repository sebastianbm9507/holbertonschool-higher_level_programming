#!/usr/bin/python3
"""
Module that creates a load_from_json_file
"""

import json


def load_from_json_file(filename):
    """Load info from json file

    Args:
        filename (str): location to read

    Returns:
        JSON: json string
    """
    with open(filename, 'r') as file:
        return json.load(file)
