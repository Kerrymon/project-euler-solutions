"""Euler Problem #32:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."""
import time
from  functools import reduce
from datetime import datetime


start_time = datetime.now()

products = {}
products = set()




for i in range(1, 2000):
    for j in range(1, 2000):
        lstofdigits = []
        i_lst = [int(x) for x in str(i)]
        j_lst = [int(y) for y in str(j)]
        i_and_j_lst  = [int(z) for z in str(i*j)]
        lstofdigits.append(i_lst)
        lstofdigits.append(j_lst)
        lstofdigits.append(i_and_j_lst)
        finalist = reduce(lambda  x,y: x+y, lstofdigits)
        finalist.sort()
        if finalist == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            products.add(i*j)
            print(i, j, i*j)
print(sum(products))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))