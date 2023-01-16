#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mod_list = []
    for x in my_list:
        if x == search:
            x = replace
        mod_list.append(x)
    return mod_list
