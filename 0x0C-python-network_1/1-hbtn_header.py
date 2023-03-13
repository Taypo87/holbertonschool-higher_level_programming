#!/usr/bin/python3
# Requests a url and displays response header value
import urllib
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info()['X-Request-Id'])
