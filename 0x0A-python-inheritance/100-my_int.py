#!/usr/bin/python3
"""
    Defines class MyInt that inherits from int
"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, x):
        """eq != is now =="""
        return not super().__eq__(x)

    def __ne__(self, x):
        """not eq == is now !="""
        return not super().__ne__(x)
