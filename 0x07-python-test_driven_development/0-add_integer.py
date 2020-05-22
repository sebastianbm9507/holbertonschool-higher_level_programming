#!/usr/bin/python3
"""
    Module with function that add two integers
"""


def add_integer(a, b=98):
    """Function that add two numbers

    Raises:
        TypeError: a parameter must be integer type
        TypeError: b parameter must be integer type
    Args:
        a (int): The first parameter.
        b (int): The second parameter.

    Returns:
        int -- a+b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        return(int(a) + int(b))
