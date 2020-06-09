#!/usr/bin/python3
"""
Module for base class
"""

import json
import os


class Base:
    """
    Base class
    """
    # class variables
    __nb_objects = 0

    @staticmethod
    def from_json_string(json_string):
        """Convert json to python object

        Args:
            json_string (json): json string

        Returns:
            json: python object
        """
        data = []
        if json_string is not None:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert python objects to json string

        Args:
            list_dictionaries (list): List of dicitionaries

        Returns:
            json: json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method that writes the json string representation of
        list_obts to a file.
        Args:
            list_objs ([list of objects]): list of cls instances
        """
        python_dict = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for x in list_objs:
                python_dict.append(x.to_dictionary())
        with open(filename, "w+", encoding="utf-8") as file:
                file.write(cls.to_json_string(python_dict))

    @classmethod
    def create(cls, **dictionary):
        """Create an instance

        Returns:
            Obj: Instance created
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads json from file

        Returns:
            list: List of dictionaries (instances)
        """
        file_name = cls.__name__ + ".json"
        list = []
        if not os.path.exists(file_name):
            return []
        else:
            with open(file_name, 'r', encoding="utf-8") as file:
                data = file.read()
                list_dict = cls.from_json_string(data)
            for dict in list_dict:
                list.append(cls.create(**dict))
            return list

    def __init__(self, id=None):
        """init method of class Base

        Args:
            id (int, optional): Unique id for every object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
