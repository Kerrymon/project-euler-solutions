"""Euler Problem #26:
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

import math
from decimal import *
from datetime import datetime


start_time = datetime.now()
def getfracpart(flnum):
    one = 1
    lstfracpart = []
    for i in range(10000):
        score = 0
        if one - flnum >= 0:
            while one - flnum >= 0:
                one = one - flnum
                score += 1
            lstfracpart.append(str(score))
        else:
            one = one * 10
    return lstfracpart


def guess_seq_len(seq):
    guess = 1
    seq = [int(i) for i in str(seq)]
    max_len = int(len(seq) / 2)
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x]:
            return x

    return guess

maximum = 1
index = 0
for i in range(2, 1001):
    listtostring = ''.join((getfracpart(i)))

    if guess_seq_len(listtostring) > maximum:
        maximum = guess_seq_len(listtostring)
        index = i

print("Maximum - ", maximum,"Index of maximum(d) - ", index)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))