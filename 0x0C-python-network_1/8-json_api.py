#!/usr/bin/python3

""" Script that takes in a letter and sends a post request """

from sys import argv
from requests import get, post

if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""

    response = post("http://0.0.0.0:5000/search_user", data=q)
    try:
        my_dict = response.json()
        id = my_dict.get('id')
        name = my_dict.get('name')
        if len(my_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(my_dict.get('id'), my_dict.get('name')))
    except:
        print("Not a valid JSON")