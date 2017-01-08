"Utilities to help solving problems."
import itertools
import functools
from collections import Counter
from operator import mul, pow

def prime_factors(num):
    """ Yield the factors of a given number."""
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            yield i
    if num > 1:
        yield num

def count_prime_factors(num):
    """ Return a collections.Counter object of all the prime factors and its
    counts."""
    return Counter(prime_factors(num))

def divisors(num):
    """ Return a sorted list of all divisors of num."""
    counts = count_prime_factors(num)
    p, p_counts = counts.keys(), counts.values()
    return sorted(
            functools.reduce(mul, map(pow, p, exponents))
            for exponents
            in itertools.product(
                    *map(lambda x: range(x+1), p_counts)
            )
    )

def prime_gen():
    """ Generate an infinite sequence of prime numbers.

    Sieve of Eratosthenes
    Code by David Eppstein, UC Irvine, 28 Feb 2002
    http://code.activestate.com/recipes/117119/
    """
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

def sliding_window(seq, size):
    " Generate sliding windows subsequence"
    for start in range(len(seq) + 1 - size):
        yield seq[start:start+size]

def triangular_gen():
    """ Generate an infinite sequence of triangular numbers."""
    tri = 0
    c = itertools.count()
    next(c)
    for i in c:
        tri += i
        yield tri
