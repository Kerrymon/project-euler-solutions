""" Euler Problem #7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

def primenum(num):
    delitel = 2
    score = 0
    while delitel != num:
        if num % delitel == 0:
            break
        else:
            score += 1
        if score == (num - delitel):
            return num
        delitel += 1


j = 1
for i in range(3, 10000000000):
    if primenum(i) == None:
        continue
    else:
        j += 1
        if j == 10001:
            print("10001-ое простое число - ", primenum(i))
            break

