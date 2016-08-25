#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import sys
import numpy as np
import atkin

def primeSieve2(upperBound):
    primes = [2]
    x = 3
    while x < upperBound:
        for p in primes[0:168]:
            if x % p == 0:
                break
        else:
            primes.append(x)
        x += 2
    return primes

def primeSieve(upperBound):
    """
    Returns a list of all prime numbers less than upperBound.
    """
    numbers = range(3, upperBound, 2)
    primes = [2]
    while numbers:
        prime = numbers.pop(0)
        primes.append(prime)
        numbers = [n for n in numbers if n % prime]
    return primes

def main():
    """
    The sum of all primes below two million.
    """
    #print 'sum of all primes less than two million = ',np.sum(primeSieve(2000000))
    #print 'sum of all primes less than two million = ',np.sum(primeSieve2(2000000))
    #print 'sum of all primes less than two million = ',np.sum(atkin.sieveOfAtkin(2000000))
    print 'sum of all primes less than two million = ',np.sum(atkin.sieveOfErat(2000000))
    
if __name__ == "__main__":
	sys.exit(main())
