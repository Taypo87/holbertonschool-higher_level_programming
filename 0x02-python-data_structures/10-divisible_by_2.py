#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = my_list[:]
    for x in new_list:
        if (x % 2 == 0):
            new_list[x] = True
        else:
            new_list[x] = False
    return new_list
