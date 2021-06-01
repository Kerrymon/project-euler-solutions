"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

import math

def search(numerator, denominator):
    division = numerator / denominator
    numlst = [int(x) for x in str(numerator)]
    denlst = [int(y) for y in str(denominator)]
    intersection = list(set(numlst) & set(denlst))
    if intersection != []:
        if len(intersection) == 1:
            commonum = intersection[0]
            for number in numlst:
                if number == commonum and len(numlst) != 1 and len(denlst) != 1:
                    numlst.remove(number)
                    denlst.remove(number)
                    if denlst[0] != 0:
                        if numlst[0]/denlst[0] == division:
                            return [numerator, denominator]
    else:
        return 0


def reduce_fraction(numer, denom):
    gen = math.gcd(numer, denom)
    return [numer//gen, denom//gen]






denmultiply = 1
numultiply = 1

for den in range(1, 100):
    for num in range(1, 100):
        if num < den:
            if search(num, den) != 0 and search(num, den) != None and num % 10 != 0 and den != 10:
                fraction = search(num, den)
                rfraction = reduce_fraction(fraction[0], fraction[1])
                denmultiply *= fraction[1]
                numultiply *= fraction[0]


print(int(denmultiply / numultiply))

