#!/usr/bin/python3

def write_file(filename="", text=""):
    """function that write text to a file"""

    with open(filename, 'w') as file:
        file.write(text)
