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
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get rectangle x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        if self.__x is not int:
            raise TypeError("x must be an integer")
        self.__x = x

    @property
    def y(self):
        """get rectangle y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        if self.__y is not int:
            raise TypeError("y must be an integer")
        self.__y = y
