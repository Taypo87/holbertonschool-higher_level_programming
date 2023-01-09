#!/usr/bin/python3
import sys
count = (len(sys.argv) - 1)
if count > 1:
    print("{:d} arguments:".format(count))
else:
    print("{:d} argument:".format(count))
for i in range(1, count + 1):
    print("{}: {}".format(i, sys.argv[i]))