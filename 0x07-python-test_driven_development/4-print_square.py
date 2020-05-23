#!/usr/bin/python3

"""This module defines the print_square function"""


def print_square(size):
    """[Function that prints a square]

    Arguments:
        size {[int]} -- [Integer value]

    Raises:
        TypeError: [size must be an integer]
        TypeError: [size must be an integer]
        TypeError: [size must be >= 0]
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
