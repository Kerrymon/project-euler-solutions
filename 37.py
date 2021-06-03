"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

import math

def is_prime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n




count = 0
result = 0
for number in range(10, 1000000000):
    lstofnumber = [int(x) for x in str(number)]
    length = len(lstofnumber)
    score = 0
    for digitsleft in range(len(lstofnumber)):
        truncking = int(''.join(str(i) for i in lstofnumber))
        if is_prime(truncking) != 0:
            score += 1
        del lstofnumber[0]
    lstofnumber = [int(x) for x in str(number)]
    for digitsright in range(len(lstofnumber)):
        truncking = int(''.join(str(i) for i in lstofnumber))
        if is_prime(truncking) != 0:
            score += 1
        lstofnumber.pop()
    if score == 2 * length:
        result += number
        count += 1
    if count == 11:
        break


print(result)