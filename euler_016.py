#!/usr/bin/env python

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import sys
import numpy as np

def orig():
    """
    My original solution to this problem.
    """
    return np.sum( [int(x) for x in str(2**1000)] )

def main():
    """
    Longest sequence for this iterative sequence.
    """
    print "sum of the digits in 2^1000 = ",orig()

if __name__ == "__main__":
	sys.exit(main())

