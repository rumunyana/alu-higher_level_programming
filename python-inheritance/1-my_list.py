#!/usr/bin/python3
'''This file creates a class that inherits from List builtin functions '''


class MyList(list):
    '''This Class inherits the built in function list'''

    def print_sorted(self):
        '''Prints the list in a sorted order  '''
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
