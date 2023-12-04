#!/usr/bin/python3
"""
Defines the peak integer algorithm
"""


def find_peak(arr):
    """
        find the peak
    """
    if arr == []:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[len(arr) - 1] >= arr[len(arr) - 2]:
        return arr[len(arr) - 1]
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
