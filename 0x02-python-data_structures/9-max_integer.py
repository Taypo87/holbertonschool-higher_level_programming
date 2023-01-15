#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    newlist = (sorted(my_list, reverse=True))
    return(newlist[0])
