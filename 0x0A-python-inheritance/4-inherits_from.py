#!/usr/bin/python3

"""Method that checks for both direct or indirect inheritance"""


def inherits_from(obj, a_class):
    """compares instance to class and subclass"""
    if isinstance(obj, a_class) or issubclass(obj, a_class) is True:
        return True
    if type(obj) is type(a_class):
        return True
    else:
        return False
