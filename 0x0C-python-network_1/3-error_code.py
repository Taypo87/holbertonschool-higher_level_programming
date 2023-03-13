#!/usr/bin/python3

""" Send request to a url then displays the bnody of the response """

from urllib import request, error
from sys import argv 

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
