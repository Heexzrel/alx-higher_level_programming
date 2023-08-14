#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    y = my_list[0]
    for x in my_list:
        if x > y:
            y = x
    return (y)
