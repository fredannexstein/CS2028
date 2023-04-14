#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:32:39 2023

@author: fred
"""

def insertion_sort(a):
    """Modifies an array contents to increasing order
    >>> x = np.array([1, 3, 6, 7])
    >>> m = insertion_sort(x)
    >>> m
    0
    >>> x = np.array([7, 6, 3, 1])
    >>> m = insertion_sort(x)
    >>> m
    9
    """   
    movect = 0
    n = len(a)
    i = 1
    while i < n:
        current = a[i]
        j = i - 1  
        while  (j >= 0) and (a[j] > current):
            a[j + 1] = a[j]; movect += 1
            j = j - 1
        if j+1 != i: a[j + 1] = current; movect += 1
        i = i + 1
    return movect
        


import numpy as np
import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

  
      