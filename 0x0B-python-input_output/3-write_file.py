#!/usr/bin/python3
"""
Module that creates a write file
"""


def write_file(filename="", text=""):
    """Function that write text in a file

    Args:
        filename (str, optional): file where to write Defaults to "".
        text (str, optional): Text to write into the file. Defaults to "".

    Returns:
        Number of characters writted
    """
    with open(filename, 'w', encoding='UTF-8') as file:
        write_lines = file.write(text)
        return write_lines
