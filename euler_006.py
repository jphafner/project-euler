#!/usr/bin/env python

"""
The sum of the squares of the first ten natural numbers is,
1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is
3025-385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""

import sys
from numpy import sqrt

def fast(n):
    """
    Sum of first n numbers = n(n+1)/2
    Sum of squares of first n numbers = n(n+1)(2n+1)/6 
    """
    return (n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6

def orig():
    """
    My original solution to this problem.
    """
    sum = 0
    sum2 = 0
    for i in range(101):
        sum += i
        sum2 += i*i
    return sum**2 - sum2

def main():
    """
    Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum.
    """
    print 'answer = ',fast(100)

if __name__ == "__main__":
	sys.exit(main())

