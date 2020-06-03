#!/usr/bin/python3
"""
    Module that creates a fucntion number_of_lines
"""


def number_of_lines(filename=""):
    """
        Function that count the number of lines from a file

    Args:
        filename (str, optional): file to be read . Defaults to "".

    Returns:
        int : Number of lines
    """
    n_lines = 0
    with open(filename, 'r') as file:
        for lines in file:
            n_lines += 1
    return(n_lines)
