#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    uniq = list(set(my_list))
    for x in uniq:
        add += x
    return (add)
