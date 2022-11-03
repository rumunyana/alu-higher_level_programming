#!/usr/bin/python3
def multiple_returns(sentence):
    x = []
    len_s = len(sentence)
    if len_s < 1:
        x.append(len_s)
        x.append("None")
    else:
        x.append(len_s)
        x.append(sentence[0])
    y = tuple(x)
    return y
