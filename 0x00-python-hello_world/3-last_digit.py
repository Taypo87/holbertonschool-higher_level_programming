#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n < 0:
    n = (n * -1)
    d = (n % 10)
    d = (d * -1)
    n = (n * -1)
else:
    d = (n % 10)
if d < 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, d))
elif d > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, d))
elif d == 0:
    print("Last digit of {} is {} and is 0".format(n, d))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, d))
