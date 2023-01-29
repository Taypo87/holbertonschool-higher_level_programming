#!/usr/bin/python3
"""task 5 for python input output"""


import json


def save_to_json_file(my_obj, filename):
    """writes object to text file in json representation"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
