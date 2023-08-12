"""Euler Problem #36:
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

"124421" "78487" "9119" "585" "77"


def binary_palindrom(num):
    binary = bin(num)
    binary = binary[2:]
    return binary == binary[-1::-1]








score = 1
result = 0
for number in range(0, 1000000):
    numberlst = [int(x) for x in str(number)]
    if binary_palindrom(number) == True:
        ispalindrom = True
        for digits in range(len(numberlst)):
            frthestart = numberlst[digits]
            frtheend = numberlst[-(digits+1)]
            if numberlst[digits] == numberlst[-(digits+1)]:
                pass
            else:
                ispalindrom = False
        if ispalindrom == True:
            print(number)
            result += number

print(result)

