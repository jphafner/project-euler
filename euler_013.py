#!/usr/bin/env python

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import sys
import numpy as np

def orig():
    """
    My original solution to this problem.
    """
    numbers = [int(x) for x in open('100-50.txt').read().splitlines()]
    return np.sum(numbers)

def main():
    """
    First ten digits of the sum of the given one-hundred 50-digit numbers.
    """
    print 'First ten digits of the sum of given numbers = ',str(orig())[:10]
    #print 'Sum of all numbers in input file = ',orig()

if __name__ == "__main__":
	sys.exit(main())

