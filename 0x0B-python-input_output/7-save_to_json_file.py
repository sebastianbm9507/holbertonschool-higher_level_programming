#!/usr/bin/python3
"""
Module
"""


import json


def save_to_json_file(my_obj, filename):
    """Function that save and obj to json file

    Args:
        my_obj (obj): Object to be save
        filename (str): Where info has to be saved
    """
    with open(filename, 'w') as file:
        jsonStr = json.dumps(my_obj)
        file.write(jsonStr)
