#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest = 0
    for key, value in a_dictionary.items():
        if biggest < value:
            biggest = value
            ret = key
    return ret
