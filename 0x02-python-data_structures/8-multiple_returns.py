#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    first = sentence[:1]
    if sentence is "":
        first = None
    tuple_ret = strlen, first
    return(tuple_ret)
