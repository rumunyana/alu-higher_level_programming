#!/usr/bin/python3
'''A script that checks if the object is an instance of a class'''


def is_kind_of_class(obj, a_class):
    '''Check if the object is an instance of a class
    Args:
        obj: object to check
        a_class: class to check from
    Returns:
        True: if the object is an instance
            of, or if the object is an instance of a class
        False: if the object is not an instance
        of, or if the object is an instance of a class
    '''
    return isinstance(obj, a_class)
