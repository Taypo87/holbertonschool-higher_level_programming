#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    unique_numbs = set(my_list)
    for i in unique_numbs:
        total = total + i
    return total
