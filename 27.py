"""Euler Problem #27:
Euler discovered the remarkable quadratic formula:
                                                n^2 + n +41
It turns out that the formula will produce 40 primes for the consecutive integer values  0 <= n <= 39. However, when
n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n +1601  was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79.
 The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b where abs(a) < 1000 and abs(b) <= 1000

where abs(n) is the modulus/absolute value of n
e.g abs(11) = 11 and abs(-4) = 4

Find the product of the coefficients, a and b for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""

import math
from datetime import datetime


start_time = datetime.now()
score = 0


def is_prime(n):
    if n < 0:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n

scoremax = 1
final = 0
a_max = 0
b_max = 0
for i in range(-1000, 1000):
    for j in range(-1001, 1001):
        for n in range(0, abs(i)):
                score = 0
                primenum =  n*n +i*n + j
                if is_prime(primenum) != 0:
                    score += 1
                else:
                    break
                if scoremax < n:
                    scoremax = n
                    final = i*j
                    a_max = i
                    b_max = j

print("max : a - ", a_max, "b - ", b_max, "a * b - ", final, "n - ", scoremax)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))