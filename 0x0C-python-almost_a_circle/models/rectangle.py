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

    # Getters

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

    # Setters

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
        if width <= 0:
            raise ValueError("width must be > 0")
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
        if height <= 0:
            raise ValueError("height must be > 0")
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
        if x < 0:
            raise ValueError("x must be >= 0")
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
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
