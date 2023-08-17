#!/usr/bin/python3

def best_score(a_dictionary):
    m = 0
    res = ""
    if a_dictionary:
        for x, y in a_dictionary.items():
            if y > m:
                res = x
                m = y
        return res
    else:
        return None
