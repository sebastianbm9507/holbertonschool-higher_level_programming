#!/usr/bin/python3
"""
    Module
"""


def inherits_from(obj, a_class):
    """Function that check if a obj inherits

    Arguments:
        obj -> Object to compare
        a_class -> Class to be compare

    Returns:
        True or False
    """
    return isinstance(obj, a_class) and not type(obj) == a_class
