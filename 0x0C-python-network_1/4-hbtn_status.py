#!/usr/bin/python3

""" Script that fetches a url status"""

import requests

if __name__ == '__main__':
    request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(request.text))
    print("\t- content:", request.text)
