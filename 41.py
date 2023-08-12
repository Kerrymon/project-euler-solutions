"""Euler Problem #41:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n

def hundred(num):
    for hun in range(2, 100):
        if num % hun == 0:
            return 1
    return 0



maximum = 0
for j in range(4, 9876543):
    if hundred(j) == 1:
        continue
    lstofi = [int(x) for x in str(j)]
    if sorted(lstofi) == [1] or sorted(lstofi) == [1, 2] or sorted(lstofi) == [1, 2, 3] or sorted(lstofi) == [1, 2, 3, 4] or sorted(lstofi) == [1, 2, 3, 4, 5] or sorted(lstofi) == [1, 2, 3, 4, 5, 6] or sorted(lstofi) == [1, 2, 3, 4, 5, 6, 7] or sorted(lstofi) == [1, 2, 3, 4, 5, 6, 7, 8] or sorted(lstofi) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if is_prime(j) > maximum:
            maximum = is_prime(j)
            print(maximum)



print(maximum)



