""" Euler Problem #4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

for sixdigitnumber in range(100000, 1000000):
    listfdn = list(str(sixdigitnumber))
    if (listfdn[0] == listfdn[5]) and (listfdn[1] == listfdn[4]) and (listfdn[2] == listfdn[3]):
        for threedigitnumber in range(100, 1000):
            if sixdigitnumber % threedigitnumber == 0 and len(list(str(int(sixdigitnumber/threedigitnumber)))) == 3:
                secondnum = int(sixdigitnumber / threedigitnumber)
                print("Число", sixdigitnumber, " делится на числа ", threedigitnumber," и ", secondnum)
