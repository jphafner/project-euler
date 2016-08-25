#!/usr/bin/env python

"""
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

import sys
import numpy as np

def is_even (x):
    return x%2==0
    
def is_odd (x):
    return x%2>0

def orig(under):
    """
    My original solution to this problem.
    """
    max = 0
    max_seq = 0
    for x in range(under/2,under):
        count = 1
        seq = x
        while seq!=1:
            if is_even(seq):
                seq = seq/2
            else:
                seq = 3*seq + 1
            count += 1
        if count>max:
            max = count
            max_seq = x
    return max_seq


    numbers = [int(x) for x in open('100-50.txt').read().splitlines()]
    return np.sum(numbers)

def main():
    """
    Longest sequence for this iterative sequence.
    """
    print 'Longest sequence = ',orig(1000000)

if __name__ == "__main__":
	sys.exit(main())

