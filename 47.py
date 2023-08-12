"""Euler Problem #47:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?"""

import math
from datetime import datetime
from functools import reduce

start_time = datetime.now()
primeslst = [x for x in range(2, 200000) if all(x % y != 0 for y in range(2, int(math.sqrt(x) + 1)))]

def is_prime(n):
    for delitel in range(2, int(math.sqrt(n) + 1)):
        if n % delitel == 0:
            return 0
    return n


print(len(primeslst))

number = 2
count = 0
lstofcombo = []
lstofdel_1 = []
lstofdel_2 = []
lstofdel_3 = []
lstofdel_4 = []
while True:
    number += 1
    num = number
    if is_prime(num) == num:
        count = 0
        lstofcombo = []
        lstofdel_1 = []
        lstofdel_2 = []
        lstofdel_3 = []
        lstofdel_4 = []
        if len(lstofcombo) > 1:
            number = lstofcombo[1]
        continue
    while num != 1:
        for prime in primeslst:
            if num % prime == 0:
                num = int(num / prime)
                if len(lstofcombo) == 0:
                    lstofdel_1.append(prime)
                if len(lstofcombo) == 1:
                    lstofdel_2.append(prime)
                if len(lstofcombo) == 2:
                    lstofdel_3.append(prime)
                if len(lstofcombo) == 3:
                    lstofdel_4.append(prime)
    if num == 1:
        lstofcombo.append(number)
    if len(set(lstofdel_1)) == len(set(lstofdel_2)) == len(set(lstofdel_3)) == len(set(lstofdel_4)) == 4:
        multiply_1 = reduce(lambda x, y: x*y, lstofdel_1)
        multiply_2 = reduce(lambda x, y: x*y, lstofdel_2)
        multiply_3 = reduce(lambda x, y: x*y, lstofdel_3)
        multiply_4 = reduce(lambda x, y: x*y, lstofdel_4)
        if len(lstofcombo) == 4 and int(lstofcombo[0] / multiply_1) == int(lstofcombo[1] / multiply_2) == int(lstofcombo[2] / multiply_3) == int(lstofcombo[3] / multiply_4):
            print(lstofcombo, lstofdel_1, lstofdel_2, lstofdel_3, lstofdel_4)
            break
    if len(lstofcombo) > 4:
        number = lstofcombo[0]
        lstofcombo = []
        lstofdel_1 = []
        lstofdel_2 = []
        lstofdel_3 = []
        lstofdel_4 = []
    print(number)

print(lstofcombo[0])










end_time = datetime.now()

print("Duration - ", end_time - start_time)