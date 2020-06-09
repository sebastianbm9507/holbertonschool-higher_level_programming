#!/usr/bin/python3
"""
Rectangle class
"""

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method for class Base

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): x axis. Defaults to 0.
            y (int, optional): y axis. Defaults to 0.
            id (int, optional): unique id . Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
    Public methods
    """

    def area(self):
        """
        Function that calculate the area of a rectangle

        Returns:
            int: area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Display the rectangle
        """
        for _ in range(self.__y):
            print("")
        for pos in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * (self.__width))

    def update(self, *args, **kwargs):
        """Update attributes for rectangle
        """
        if args is not () and args is not None:
            attr_names = ["id", "width", "height", "x", "y"]
            for index, attr in enumerate(args):
                setattr(self, attr_names[index], attr)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """__str__ method

        Returns:
            str: String format
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """Represent object in dictionary

        Returns:
            dict: Dictionary representation
        """
        new_dictionary = {}
        for key, value in self.__dict__.items():
            new_dictionary[key.split("__")[-1]] = value
        return new_dictionary

    """
    Properties
    """

    @property
    def width(self):
        """getter to width
        """
        return self.__width

    @property
    def height(self):
        """getter to height
        """
        return self.__height

    @property
    def x(self):
        """getter to x
        """
        return self.__x

    @property
    def y(self):
        """
        getter to y
        """
        return self.__y

    """
    Setters
    """

    @width.setter
    def width(self, width):
        """Widht setter

        Args:
            width (int): width of rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """Height setter

        Args:
            height (int): height of rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """X setter

        Args:
            x (int): X coordenate of rectangle

        Raises:
            TypeError: x must be an integer
            ValueError: x must be > 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """Y setter

        Args:
            y (int): y coordenate of rectangle

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
