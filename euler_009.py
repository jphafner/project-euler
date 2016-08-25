#!/usr/bin/env python

"""
Find the greatest product of five consecutive digits in the 1000-digit number.

Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^(2) + b^(2) = c^(2)
 
For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
 
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
Number is located in euler_008.txt.
"""

import sys
import numpy as np

def fast(sum):
    """
    http://www.math.uic.edu/~fields/puzzle/triples.html
    """
    n = int( ( 1 + np.sqrt(1+4*sum) ) / 4 )
    while True:
        m = sum/2/n - n 
        triplet = [n**2-m**2, 2*m*n, n**2+m**2]
        if np.sum(triplet) == 1000:
            return triplet
        n+=1

def one_line():
    return [(x,y,1000-x-y) for x in range(1,1000) for y in range(1,x) if x**2+y**2==(1000-x-y)**2]

def orig():
    """
    My original solution to this problem.
    """
    for a in range(1,500):
        for b in range(a+1,500):
            if a+b+np.sqrt(a**2+b**2)==1000:
                print "a=%d, b=%d, c=%d" % (a,b,np.sqrt(a**2+b**2))
                print "a*b*c = %d" % (a*b*np.sqrt(a**2+b**2))
                return a*b*np.sqrt(a**2+b**2)

def main():
    """
    Find the product of abc where a^2+b^2=c^2 and a+b+c=1000.
    """
    triplet = fast(1000)
    print "First pythagorean triplet to sum to 1000 is ", triplet
    print "Its product is ",np.prod(triplet)
    #orig()

if __name__ == "__main__":
	sys.exit(main())

