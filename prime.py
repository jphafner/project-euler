#!/usr/bin/env python

message = """
 prime.py - Finds first ten digit prime in sequence of
            numbers provided in input file.

 Syntax  : prime.py <digit file>

 Example : prime.py e10000.dat
"""

import sys
from numpy import sqrt

def is_prime (x):
    return all (x%i>0 for i in range(3,int(sqrt(x)+1),2))

def is_even (x):
    return x%2==0

def is_odd (x):
    return x%2>0

def find_prime( numstr, length ):
    for i in range(0, len(numstr)-length):
        num = int( numstr[i:i+length] )
        if is_odd(num):
            if is_prime(num):
                return num

def main():
    numstr = open(sys.argv[1],"r").readline()
    print find_prime( numstr, 10 )

if __name__ == "__main__":
    if len(sys.argv)==2:
        main()
    else:
        print message

