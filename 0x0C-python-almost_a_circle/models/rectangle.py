#!/usr/bin/python3
"""Rectangle class for almost a circle project"""


from models.base import Base


class Rectangle(Base):
    """Class Recatngle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing attributes for class Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """width setter"""
        if not isinstance(self.__height, int):
            raise TypeError("width must be an integer")
        if not isinstance(self.__height, bool):
            raise TypeError("width must be an integer")
        if self.__height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @property
    def x(self):
        """get rectangle x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """get rectangle y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y
