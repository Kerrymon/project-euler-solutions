"""Euler Problen #46:
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""

import math
primeslst = [x for x in range(2, 100000) if all(x % y != 0 for y in range(2, int(math.sqrt(x) + 1)))]

def is_not_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return n
    return 0


double_squares_lst = []
for double_squares in range(1, 10000):
    double_squares_lst.append(2*double_squares*double_squares)


for i in range(3, 100000):
    if i % 2 == 0 or is_not_prime(i) == 0:
        continue
    number = False
    for prime in primeslst:
        for twice_square in double_squares_lst:
            if prime + twice_square > i:
                break
            if prime + twice_square == i:
                number = True
                print("For ", i, "found ", prime, "+", twice_square)
                break
    if number == False:
        print("Found mistake on ", i)
        break






    



