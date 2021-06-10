""" Euler Problem #4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


# looking for a number from 100000 to 1 million
for sixdigitnumber in range(100000, 1000000):
    # split number to list
    listfdn = list(str(sixdigitnumber))
    # if number is palindromic
    if (listfdn[0] == listfdn[5]) and (listfdn[1] == listfdn[4]) and (listfdn[2] == listfdn[3]):
        # bruteforce scan two multipliers
        for threedigitnumber in range(100, 1000):
            # if palindromic number is dividing to one multiplier number without a remainder
            if sixdigitnumber % threedigitnumber == 0 and len(list(str(int(sixdigitnumber/threedigitnumber)))) == 3:
                # find second multiplier
                secondnum = int(sixdigitnumber / threedigitnumber)
                # print all, last is the biggest
                print("Число", sixdigitnumber, " делится на числа ", threedigitnumber," и ", secondnum)
