"""Euler Problem #23:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

from functools import  reduce
from datetime import datetime


start_time = datetime.now()
def dividers(N):
    D = [1]  # список делителей
    d = 2  # делитель
    while (d * d <= N):
        if N % d == 0:
            D = D + [d]
            d_new = N // d
            if d_new != d:
                D = D + [d_new]

        # следующий делитель
        d += 1

    result = reduce(lambda x, y: x+y, D)

    return result



final = 0
rez = 0
for number in range(1, 28123):
    for i in range(number):
        b = number - i
        if dividers(i) > i and dividers(b) > b and  b!= 0 and i != 0:
            final += number
            break
    rez += number

print(rez - final)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))