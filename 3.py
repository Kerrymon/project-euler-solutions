""" Euler Problem #3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from functools import reduce

largenumber = 600851475143
newlargenumber = 0
primearr = []
bfnumber = 1
score = 0
while newlargenumber != 1:
    bfnumber += 1
    if largenumber % bfnumber == 0:
        for delitel in range(2, bfnumber + 1):
            if bfnumber % delitel == 0 and not bfnumber == delitel:
                break
            else:
                if bfnumber == delitel:
                    primearr.append(bfnumber)
                    print(bfnumber, "- простое число")
                    break
        multiprime = reduce(lambda x, y: x*y, primearr)
        newlargenumber = int(largenumber / multiprime)
        print("новое большое число - ", newlargenumber)

print("\nСамое большое простое число -", max(primearr))