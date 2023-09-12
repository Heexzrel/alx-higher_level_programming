#!/usr/bin/python3
"""
    is_same_class module
"""


def is_same_class(obj, a_class):
    """
    check instance and class
    Return: True or False
    """
    return type(obj) is a_class
