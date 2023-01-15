#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    firstl = sentence[:1]
    if sentence is "":
        firstl = None
    tuple_ret = strlen, firstl
    return(tuple_ret)
