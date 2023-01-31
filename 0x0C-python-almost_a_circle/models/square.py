#!/usr/bin/python3
"""Class square inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represnts a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        self.__size = size


def __str__(self):
        """String Informal of the Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.__x,
                                                         self.__y,
                                                         self.__size)
