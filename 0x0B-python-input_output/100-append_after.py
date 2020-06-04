#!/usr/bin/python3
"""Module for apped_after"""


def append_after(filename="", search_string="", new_string=""):
    """Insert after match a string

    Args:
        filename (str, optional): file name. Defaults to "".
        search_string (str, optional): string to search into file. Defaults "".
        new_string (str, optional): string to be add. Defaults to "".
    """
    with open(filename, 'r',  encoding='utf-8') as file:
        data = file.readlines()

    str = ""
    for line in data:
        str = str + line
        if search_string in line:
            str = str + new_string
    with open(filename, 'w',  encoding='utf-8') as file:
        f.write(str)
