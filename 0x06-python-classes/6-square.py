#!/usr/bin/python3


"""
This module creates a new class Square
"""


class Square:
    """ __init__ method class """
    def __init__(self, size=0, position=(0,0)):
            self.__size = size
            self.__position = position

    def area(self):
        """ Return the area of square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Return size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of square """
        if (type(value) != int):
            raise ValueError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """ Print a square """
        if self.__size is 0:
            print("")
        else:
            for m in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print('#', end="")
                print("")

    @property
    def position(self):
        """ Return position """
        return self.__position

    @position.setter
    def position(self, value):
        """Setv value """

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
