#!/usr/bin/python3

""" Script that takes in a URL and displays the value of the X-Request-Id """

from sys import argv
import requests

if __name__ == '__main__':
    request = requests.get(argv[1])
    print(request.headers.get("X-Request-Id"))
