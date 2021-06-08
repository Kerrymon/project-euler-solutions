"""Euler Problem #49:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""

from itertools import permutations
import math

def is_prime(num):
    for delitel in range(2, int(math.sqrt(num) + 1)):
        if num % delitel == 0:
            return 0
    return num





for number in range(1000, 9999):
    lstnumber = [int(x) for x in str(number)]
    perm = permutations(lstnumber)
    blanklst = []
    for i in list(perm):
         blanklst.append(int(str(i[0]) + str(i[1]) + str(i[2]) + str(i[3])))
    for data in blanklst:
        for permutation_1 in blanklst:
            for permutation_2 in blanklst:
                bestofthree = [data, permutation_1, permutation_2]
                bestofthree.sort()
                if data != permutation_1 or data != permutation_2 or permutation_1 != permutation_2:
                    if is_prime(data) == data and is_prime(permutation_2) == permutation_2 and is_prime(permutation_1) == permutation_1 and bestofthree[2] - bestofthree[1] == bestofthree[1] - bestofthree[0] and bestofthree[0] // 1000 != 0 and bestofthree[1] // 1000 != 0 and bestofthree[2] // 1000 != 0:
                        print(data, permutation_1, permutation_2)