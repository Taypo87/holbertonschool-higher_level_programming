#!/usr/bin/python3

"""Script takes a url request and displays Id"""

from sys import argv
import requests

request = requests.get(argv[1])
print(request.headers.get("X-Request-Id"))
