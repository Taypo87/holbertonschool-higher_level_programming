#!/usr/bin/python3
""" script that takes github credentials and displays the id """
from sys import argv
import requests

if __name__ == '__main__':
    try:
        request = requests.get("https://api.github.com/user",auth=(argv[1], argv[2]))
        print(request.json()["id"])
    except:
        print("None")
