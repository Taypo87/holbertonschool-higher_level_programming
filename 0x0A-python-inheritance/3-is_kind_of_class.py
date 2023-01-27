#!/usr/bin/python3

"""method to check if object is an instance of given Class"""


def is_kind_of_class(obj, a_class):
    """function to compare instance to Class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
