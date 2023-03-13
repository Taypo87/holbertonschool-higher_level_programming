#!/usr/bin/python3

"""Sends Post request to passed url, with email as a parameter"""

from sys import argv
import requests

if __name__ == "__main__":
    email = {"email": argv[2]}
    request = requests.post(argv[1], data=email)

    print(request.text)
