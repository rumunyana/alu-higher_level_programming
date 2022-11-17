#!/usr/bin/python3
''' a function that returns True if the object is
an instance of a class that inherited (directly or indirectly)'''


def inherits_from(obj, a_class):
    '''Function to check the object
    Args:
        obj: the object
        a_class: the class
    Returns:
        True: if the object is an instance
        False: if the object isn't an instance
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
