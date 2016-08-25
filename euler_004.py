#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palildrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys
from numpy import sqrt

def orig():
    """
    My original solution to this problem.
    """
    p = 0
    n = str(p)
    for i in range(100,1000):
        for j in range(i,1000):
            n = str(i*j)
            if n==n[::-1]:
                p = max(p,int(n))
    return p

def main():
    """
    Print the largest palidrome made from the product of two 3-digit numbers.
    """
    print "largest palidrome is ",orig()

if __name__ == "__main__":
	sys.exit(main())

