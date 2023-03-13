#!/usr/bin/python3

""" Script that takes a url, sends a request
                 and displays the id from the response header"""

from sys import argv
import requests

request = requests.get(argv[1])
print(request.headers.get("X-Request-Id"))
