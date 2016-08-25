#!/usr/bin/env python

"""
Starting in the top left corner ofa 2x2 grid, there are 6 routes (without backtracking)
to the bottom right corner.

How many routes are there through a 20x20 grid?
"""

import sys
import numpy as np

def binom(n, m):
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n+1):
        b[i] = 1
        j = i - 1
        while j > 0:
            b[j] += b[j-1]
            j -= 1
    return b[m]

def main():
    """
    Routes through a 20x20 grid.
    """
    print "Routes through a 20x20 grid = ",binom(40,20)

if __name__ == "__main__":
	sys.exit(main())

