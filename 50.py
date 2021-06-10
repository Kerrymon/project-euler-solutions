"""Euler Problem #50:
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""

import math
from datetime import datetime

start_time = datetime.now()

def is_prime(num):
    for delitel in range(2, int(math.sqrt(num) + 1)):
        if num % delitel == 0:
            return 0
    return num


prime_lst = [x for x in range(2, 10000) if all(x % y != 0 for y in range(2, int(math.sqrt(x) + 1)))]
print(len(prime_lst))

maximum = 0
maxindex = 0
for i in range(3, 1000000, 2):
    for index in range(0, 4):
        is_not_chain = True
        sumnum = 0
        count = 0
        while is_not_chain:
            sumnum += prime_lst[index]
            index += 1
            count += 1
            if sumnum > i:
                break
            if sumnum == i:
                is_not_chain = False
                break
            if index == len(prime_lst)-1:
                continue

        if is_not_chain == False and count > maximum and is_prime(i) == i:
            maxindex = i
            maximum = count
            break


    print(i)
print(maximum, maxindex)

end_time = datetime.now()
print("Duration  - ", end_time - start_time)







