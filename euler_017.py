#!/usr/bin/env python

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?
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
    Amount of letters used in printing 1 to 1000.
    """
    print "Amount of letters used in printing 1 to 1000 = ",orig()

if __name__ == "__main__":
	sys.exit(main())

