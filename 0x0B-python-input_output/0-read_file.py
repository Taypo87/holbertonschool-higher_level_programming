#!/usr/bin/python3
"""function that opens file and writes to stdout"""


def read_file(filename=""):
    """opens file and prints to stdout"""
    r = with open(filename)
    print(r.read())
