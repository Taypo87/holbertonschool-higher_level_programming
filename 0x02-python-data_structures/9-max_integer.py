#!/usr/bin/python3
def max_integer(my_list=[]):
    newlist = (sorted(my_list, reverse=True))
    return(newlist[0])