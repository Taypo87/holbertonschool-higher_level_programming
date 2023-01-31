#!/usr/bin/python3
'''Rectangle Class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Inicilizating ATRIBUTES
        Inheriting attribute ID'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.check_wh("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.check_wh("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.check_xy("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.check_xy("y", y)
        self.__y = y

    def check_wh(self, n, a):
        '''Method that check the values of width and height'''
        if type(a) is not int:
            raise TypeError("{} must be an integer".format(n))
        if a <= 0:
            raise ValueError("{} must be > 0".format(n))
        return

    def check_xy(self, n, a):
        '''Method that check the values of x and y'''
        if type(a) is not int:
            raise TypeError("{} must be an integer".format(n))
        if a < 0:
            raise ValueError("{} must be >= 0".format(n))
        return
