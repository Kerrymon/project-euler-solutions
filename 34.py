"""Euler Project #34:
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included."""


def fact(num):
    factorial = 1
    if num == 0:
        return 1
    while num != 1:
        factorial *= num
        num = num - 1
    return factorial


sumofn = 0
for i in range(3, 100000):
    sumofact = 0
    res = [int(x) for x in str(i)]
    for result in res:
        sumofact += fact(result)
    if sumofact == i:
        sumofn += i

print(sumofn)

