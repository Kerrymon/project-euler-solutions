"""Euler Problem #31:
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""

from datetime import datetime


start_time = datetime.now()


def usl(balance, thebiggest):
    if thebiggest >= two_e: check(balance, two_e)
    if thebiggest >= one_e: check(balance, one_e)
    if thebiggest >= fifty_p: check(balance, fifty_p)
    if thebiggest >= twenty_p: check(balance, twenty_p)
    if thebiggest >= ten_p: check(balance, ten_p)
    if thebiggest >= five_p: check(balance, five_p)
    if thebiggest >= two_p: check(balance, two_p)
    if thebiggest >= one_p: check(balance, one_p)


def check(balance, moneta):
    global count
    balance += moneta
    if balance == two_e:
        count += 1
    elif balance < two_e:
        usl(balance, moneta)


def value():
    balance = 0
    thebiggest = two_e
    usl(balance, thebiggest)
    return count

if __name__ == '__main__':
    count = 0
    one_p = 1
    two_p = 2
    five_p = 5
    ten_p = 10
    twenty_p = 20
    fifty_p = 50
    one_e = 100
    two_e = 200
    print(value())

end_time = datetime.now()
print("Duration -  ", end_time - start_time)