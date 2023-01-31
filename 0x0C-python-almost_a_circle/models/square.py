#!/usr/bin/python3
"""Class square inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represnts a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        """size setter"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size


    def __str__(self):
        """String Informal of the Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.__x,
                                                         self.__y,
                                                         self.__width)
    def update(self, *args, **kwargs):
        '''Method that assigns a value to each attribute'''
        key = ["id", "size", "x", "y"]
        if len(args) > 0:
            for x in range(len(args)):
                setattr(self, key[x], args[x])
        else:
            for a in kwargs:
                setattr(self, a, kwargs[a])

    def to_dictionary(self):
        '''Method that returns the dictionary representation of a Square'''
        key = ["id", "size", "x", "y"]
        value = [self.id, self.size, self.x, self.y]
        return dict(zip(key, value))
