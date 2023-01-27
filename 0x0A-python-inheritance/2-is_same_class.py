#!/usr/bin/python3
"""function is_same_class reurns true or false"""


def is_same_class(obj, a_class):
    """checks if object is an instance of Class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
