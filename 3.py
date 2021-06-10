""" Euler Problem #3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from functools import reduce
import math

def is_prime(num):
    for delitel in range(2, int(math.sqrt(num) + 1)):
        if num % delitel == 0:
            return 0
    return num


largenumber = 600851475143
number = largenumber
primearr = []
bfnumber = 1

# looking for prime divisors in the loop
while largenumber != 1:
    bfnumber += 1
    if largenumber % bfnumber == 0 and is_prime(bfnumber) == bfnumber:
        primearr.append(bfnumber)
        print(bfnumber, "- prime number")
        largenumber = int(largenumber / bfnumber)

# multiply everything in primearr
multiprime = reduce(lambda x, y: x*y, primearr)
number = int(number / multiprime)
print("new big number - ", number)

print("\nthe biggest prime number -", max(primearr))