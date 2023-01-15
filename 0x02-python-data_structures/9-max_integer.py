#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    newlist = (sorted(my_list, reverse=True))
    return(newlist[0])
