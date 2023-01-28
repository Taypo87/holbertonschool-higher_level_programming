#!/usr/bin/python3
"""function that opens file and writes to stdout"""


def read_file(filename=""):
    """opens file and prints to stdout"""
    with open(filename, 'r') as file:
        print(file.read())
