#!/usr/bin/python3
"""

This module contains a function that adds two numbers

"""


def add_integer(a, b=98):
    """
    Function that adds two floats or integers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of two numbers

    Raises:
        TypeError: If a or b aren't Integers or Floats
    
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an int")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an int")
    return (int(a) + int(b))
