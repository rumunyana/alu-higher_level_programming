#!/usr/bin/python3
""""Peak"""


def find_peak(list_of_integers):
    """Finds the peak"""
    list_of_integers.sort()
    return list_of_integers[-1]
