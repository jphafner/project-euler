#!/usr/bin/env python

"""
Find the greatest product of five consecutive digits in the 1000-digit number.

Number is located in euler_008.txt.
"""

import sys
from numpy import sqrt

def fancy(length,filename):
    from string import whitespace
    from operator import mul
     
    data = open(filename) # Number pasted to file.
    nos = [int(c) for line in data for c in line if c not in whitespace]
    return max([reduce(mul, nos[i:i+length]) for i in range(len(nos)-length)])

def orig(length, filename):
    """
    My original solution to this problem.
    """
    product=0
    numstr = open(filename,"r").readline()
    for i in range(0, len(numstr)-length):
        num = int(numstr[i])
        for j in range(1,length):
            num *= int( numstr[i+j] )
        if num > product:
            product=num
    return product

def main():
    """
    Print greatest product of five consecutive digits from a given sequence of numbers.
    """
    print 'orig = ',orig(5,"euler_008.txt")
    print 'fancy = ',fancy(5,"euler_008.txt")

if __name__ == "__main__":
	sys.exit(main())

