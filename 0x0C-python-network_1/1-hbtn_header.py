#!/usr/bin/python3

import urllib
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info()['X-Request-Id'])
