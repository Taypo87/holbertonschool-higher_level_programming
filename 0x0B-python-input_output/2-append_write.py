#!/usr/bin/pyhton3
"""Task 2 for Python input output"""


def append_write(filename="", text=""):
    """appends a text file with given string"""

    with open(filename, 'a') as file:
        file.write(text)
