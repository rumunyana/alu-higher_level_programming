#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    leng_a, leng_b = len(tuple_a), len(tuple_b)
    if leng_a == 0:
        a = (0, 0)
    elif leng_a == 1:
        a = (tuple_a[0], 0)
    else:
        a = tuple_a
    if leng_b == 0:
        b = (0, 0)
    elif leng_b == 1:
        b = (tuple_b[0], 0)
    else:
        b = tuple_b
    return (a[0] + b[0], a[1] + b[1])
