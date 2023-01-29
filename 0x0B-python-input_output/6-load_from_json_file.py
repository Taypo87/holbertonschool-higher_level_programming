#!/usr/bin/python3
"""task 5 for python input output"""


import json

def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
