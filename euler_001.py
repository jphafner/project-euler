#!/usr/bin/env python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys
from numpy import sqrt

def analytic():
    """
    This problem has an analytic solution.
    """
    return mcp1(3, 999) + mcp1(5, 999) - mcp1(15, 999)

def mcp1(n, m):
    """
    Return sum of all numbers that are multiples of n less than m.
    """
    f = m / n
    return n * f * (f + 1) / 2

def orig():
    """
    My original solution to this problem.
    """
    sum = 0
    for i in range(3,1000):
        if i%3==0 or i%5==0:
            sum+=i
    return sum

def main():
    """
    Print sum of all natural numbers that are multiples of 3 or 5 that are below 1000.
    """
    print 'original solution = ',orig()
    print 'analytic solution = ',analytic()

if __name__ == "__main__":
	sys.exit(main())
