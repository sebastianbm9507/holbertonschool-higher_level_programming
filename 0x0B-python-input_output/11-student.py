#!/usr/bin/python3
"""
Module that create a Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """Init method

        Args:
            first_name (str): Student First name
            last_name (str): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Represent a instance in dict form

        Returns:
            obj: instance in dict form represented
        """
        return (self.__dict__)
