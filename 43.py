"""Euler Problem #43:
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""

import itertools




def fact(num):
    factorial = 1
    while num != 1:
        factorial *= num
        num = num - 1
    return factorial


print(fact(10))


print(list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])).index((1, 4, 0, 6, 3, 5, 7, 2, 8, 9)))

lstofnumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
allpermutationslst = list(itertools.permutations(lstofnumbers))
print(allpermutationslst[1])
lstofprime = [2, 3, 5, 7, 11, 13, 17]

result = 0
for permutation in range(0, fact(10)):
    numbertuple = allpermutationslst[permutation]
    numberint = ''
    for build in range(0, 10):
        numberint += str(numbertuple[build])
    numberint = int(numberint)
    numper = True
    for d in range(0, 7):
        if int(str(numbertuple[d+1])+str(numbertuple[d+2]) + str(numbertuple[d+3])) % lstofprime[d] != 0:
            numper = False
            break
    if numper == True:
        result += numberint
        print(numberint)


print(result)
