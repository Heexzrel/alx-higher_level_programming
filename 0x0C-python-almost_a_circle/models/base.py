#!/usr/bin/python3
"""Base Module"""
import json
import csv


class Base:
    """
    The Base Class with
    Attributes: __nb_object : private class atribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init Attributes:
            id (): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
