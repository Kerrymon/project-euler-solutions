"""Euler Problem #16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""
from functools import reduce

bignumber = 2**1000

lstbignumber = list(str(bignumber))

lstbignumber = [int(i) for i in lstbignumber]

print(type(lstbignumber[5]))

sumoflst = reduce(lambda x, y: x+y, lstbignumber)
print(sumoflst)
