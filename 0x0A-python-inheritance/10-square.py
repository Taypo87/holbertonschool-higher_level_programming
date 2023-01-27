#!/usr/bin/python3

"""Task Rectangle class"""


class BaseGeometry:
    """Class methods to verify types"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class rectangle, defines shape"""

    def __init__(self, width, height):
        """defines height and width of a rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):
    """Class Square defines size"""

    def __init__(self, size):
        """Method defining size of Square instance"""

        super().integer_validator("size", size)
        self.__size = size

    def area(self, size):
        return self.__size * self.__size
