#!/usr/bin/python3
"""
    Module that creates a BaseGeometry class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[summary]

    Arguments:
        Rectangle {[type]} -- [description]
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)