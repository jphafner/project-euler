#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import sys
from numpy import sqrt

def max_prime_factor(n):
    d=2
    while d < n/d:
        if n%d==0:
            n/=d
        else:
            d+=1
    return n

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

def readPrime(filename):
    """
    Returns an array of numbers from file.
    prime-numbers.org gives such lists.
    """
    primes = []
    for line in open(filename,"r").readlines():
        primes.append(int(line))
    return primes

def orig(number):
    """
    My original solution to this problem.
    """
    primes = primeSieve(int(number**0.5)+1)
    #primes = readPrime("prime-list.txt")
    factor = 0
    for i in primes:
        if number%i==0:
            factor = i
    return factor

def main():
    """
    Print the largest prime factor of 600851475143.
    """
    #print "largest prime factor is ",orig(600851475143)
    print "largest prime factor is ",max_prime_factor(600851475143)
            
if __name__ == "__main__":
	sys.exit(main())
