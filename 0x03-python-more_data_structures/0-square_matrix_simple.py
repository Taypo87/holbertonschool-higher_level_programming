#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for x in matrix:
        squares.append(list(map(lambda x: x**2, x)))
    return squares
