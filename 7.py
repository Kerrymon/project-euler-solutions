""" Euler Problem #7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from datetime import datetime

import math
start_time = datetime.now()

# function that checks number on prime
def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return n


j = 1
# check every odd number prime it or not
for i in range(3, 10000000000, 2):
    if is_prime(i) == 0:
        continue
    else:
        j += 1
        if j == 10001:
            print("10001-ое простое число - ", is_prime(i))
            break

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))