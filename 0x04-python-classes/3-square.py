#!/usr/bin/python3

"""Class documentation"""


class Square:
    """class Square with private instance attribute size
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self. __size
        
    @size.setter
    def size(self,size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """
    Return area of a square
    """
    def area(self):
        return (self.__size * self.__size)
