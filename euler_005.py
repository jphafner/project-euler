#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of
the numbers from 1 to 20?
"""

import sys
from numpy import sqrt

def orig():
    """
    My original solution to this problem.
    """
    x = 19*20
    max = 20*19*18*17*16*15*14*13*12*11
    while not all (x%i==0 for i in range(11,21)):
        x+=19*20
        if x>max:
            print "broken"
            break
    return x

def main():
    """
    Print smallest number that is evenly divisible by all numbers from 1 to 20.
    """
    print 'smallest number = ',orig()

if __name__ == "__main__":
	sys.exit(main())

