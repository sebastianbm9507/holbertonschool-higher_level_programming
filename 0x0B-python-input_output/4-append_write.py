#!/usr/bin/python3
"""
Module that creates a append_write function
"""


def append_write(filename="", text=""):
    """Function that append text in a file

    Args:
        filename (str, optional): file where to write Defaults to "".
        text (str, optional): Text to write into the file. Defaults to "".

    Returns:
        Number of characters writted
    """
    with open(filename, 'a', encoding='utf-8') as file:
            write_lines = file.write(text)
            return write_lines
