#!/usr/bin/python3
'''A function that returns the available atts and methods of an object '''


def lookup(obj):
    '''Take an object and return its atts and methods'''
    return list(dir(obj))
