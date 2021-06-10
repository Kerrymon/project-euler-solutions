"""Euler Problem #10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n


sumn = 0
# check every num: prime is it?
for i in range(2, 2000000):
    sumn += is_prime(i)

print(sumn)