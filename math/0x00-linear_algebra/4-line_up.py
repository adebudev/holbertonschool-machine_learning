#!/usr/bin/env python3
""" Line Up """


def add_arrays(arr1, arr2):
    """ add two arrays """

    new_array = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            new_array.append(arr1[i] + arr2[i])
        return new_array
    else:
        return None
