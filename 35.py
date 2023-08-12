"""Euler Problem #35:
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

import math
import numpy
from datetime import datetime


start_time = datetime.now()

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n



count = 0
for number in range(2, 1000000):
    lstofnumber = [int(x) for x in str(number)]
    score = 0
    for digit in range(len(lstofnumber)):
        rotatedlst = numpy.roll(lstofnumber, digit)
        rotatednumber = int(''.join(str(i) for i in rotatedlst))
        if is_prime(rotatednumber) != 0:
            score += 1
        if score == len(lstofnumber):
            count += 1

print(count)



end_time = datetime.now()

print("Duration  - ", end_time - start_time)


