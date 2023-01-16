#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbs = set(my_list)
    for i in range(0, len(unique_numbs)):
        total = total + unique_numbs[i]
    return total
