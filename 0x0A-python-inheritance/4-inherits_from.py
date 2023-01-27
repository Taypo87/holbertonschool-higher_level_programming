#!/usr/bin/python3

"""Method that checks for both direct or indirect inheritance"""


def inherits_from(obj, a_class):
    """compares instance to class and subclass"""

    return type(obj) != a_class and isinstance(obj, a_class)
