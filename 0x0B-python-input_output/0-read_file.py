#!/usr/bin/python3
"""
    Module that creates a read_file function
"""


def read_file(filename=""):
    """Read a file content

    Args:
        filename (str, optional): file to be read. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    print(data, end="")
