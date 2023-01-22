#!/usr/bin/python3

""" Rectangle Class """


class Rectangle:
    """ Class rectangle with private instance attribute width, heigth """

    def __init__(self, width=0, height=0):
        """method: __init__
        initialzie instance of Rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method: set_width getter
        """
        if (not isinstance(self.__width, int)) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        """method: set_width setter
        """
        if (not isinstance(self.__width, int)):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

    @property
    def height(self):
        """method: set height getter
        """
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__heigth

    @height.setter
    def height(self, height):
        """method: set_height setter"""
        if (not isinstance(self.__height, int)):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = height
