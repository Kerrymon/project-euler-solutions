"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""
from datetime import datetime

start_time = datetime.now()

def sumofdelit(num):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i

    return result

final = 0
for j in range(0, 10000):
    if j == sumofdelit(sumofdelit(j)) and j != sumofdelit(j):
        final += j

print(final)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))