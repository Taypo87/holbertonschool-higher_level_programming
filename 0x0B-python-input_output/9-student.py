#!/usr/bin/python3
"""task 9 for pyhton input output"""


class Student:
    """student class defining name and age"""

    def __init__(self, first_name, last_name, age):
        """method init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method to_json'''

        return self.__dict__
