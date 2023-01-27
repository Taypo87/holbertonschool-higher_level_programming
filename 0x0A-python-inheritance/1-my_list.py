#!/usr/bin/python3
"""Task 1 for inheritance"""


class MyList(list):
    """Mylist Class"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
