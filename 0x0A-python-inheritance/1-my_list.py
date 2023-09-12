#!/usr/bin/python3
"""
    module inherit list
"""


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ Print a sorted List """
        print(sorted(self))
