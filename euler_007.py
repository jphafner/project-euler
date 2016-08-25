#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6^(th) prime is 13.

What is the 10001^(st) prime number?
"""

import sys
from numpy import sqrt

def primeSieve(length,upperBound):
    """
    Returns a list of all prime numbers less than upperBound.
    """
    numbers = range(3, upperBound, 2)
    primes = [2]
    while numbers:
        prime = numbers.pop(0)
        primes.append(prime)
        numbers = [n for n in numbers if n % prime]
    return primes[length]

def orig(length):
    """
    My original solution to this problem.
    """
    primes = [2,3,5,7,11,13,15,17,19,23,29]
    number = 31
    while len(primes)<=length:
        if all (number%x>0 for x in primes):
            primes.append(number)
        number+=2
    return max(primes)

def main():
    """
    Print 10001st prime number.
    """
    #print 'answer = ',orig(10001)
    print 'answer = ',primeSieve(10001,int(1e6))

if __name__ == "__main__":
	sys.exit(main())

