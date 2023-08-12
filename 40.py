"""Euler Problem #40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""


champernowne = [0]

for number in range(1, 100000):
    lstofi = [int(x) for x in str(number)]
    champernowne += lstofi

print(champernowne[1] * champernowne[10] * champernowne[100] * champernowne[1000] * champernowne[10000] * champernowne[100000])