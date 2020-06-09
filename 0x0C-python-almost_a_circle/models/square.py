#!/usr/bin/python3

"""
Modulo from Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle

    Args:
        Rectangle (obj): Parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init method

        Args:
            size (int): size of square
            x (int, optional): x coordinate of square. Defaults to 0.
            y (int, optional): y coordinate of square. Defaults to 0.
            id (optional): id of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update the attributes of an instance
        """
        if args is not () and args is not None:
            attr_names = ["id", "size", "x", "y"]
            for index, attr in enumerate(args):
                setattr(self, attr_names[index], attr)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Represent object in dictionary

        Returns:
            dict: Dictionary representation
        """
        new_dictionary = {}
        for key, value in self.__dict__.items():
            new_dictionary[key.split("__")[-1]] = value
        new_dictionary['size'] = new_dictionary['width']
        del new_dictionary['width']
        del new_dictionary['height']
        return new_dictionary

    @property
    def size(self):
        """Getter

        Returns:
            int: size of the rectangle
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter
        """
        self.width = size
        self.height = size

    def __str__(self):
        """String representation of square

        Returns:
            string: representation of square
        """
        return "[Square] ({}) {}/{} - {}\
        ".format(self.id, self.x, self.y, self.width)
