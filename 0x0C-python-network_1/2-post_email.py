#!/usr/bin/python3

""" takes in a url, sends post request, displays body as response"""

import sys
from urllib import request, parse

if __name__== '__main__':

    data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
