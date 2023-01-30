#!/usr/bin/python3
"""Task 8 for python input output"""


def class_to_json(obj):
    """ returns a dictionary representation for json serialization of object"""

    return obj.__dict__
