#!/usr/bin/python3
"""

This module contains a method to divide a matrix by a given number

"""
def matrix_divided(matrix, div):
    """
    Method that divides the int/float of a matrix

    """
    if type(matrix) is not list:
        raise TypeError("Must be a matrix of ints and floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("Must be a matrix of ints and floats")
        if size is None:
                size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return[[round(i / div, 2)for i in x] for x in matrix]
    