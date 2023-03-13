#!/usr/bin/python3
""" Script that takes in a URL and displays the value of the X-Request-Id """

import urllib
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
