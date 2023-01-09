#!/usr/bin/python3
import sys
count = (len(sys.argv) - 1)
if count > 1:
    print("{:d} arguments:".format(count))
else:
    print("{:d} argument:".format(count))
