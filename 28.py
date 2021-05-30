"""Euler Problem #28:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""


score_1 = 1
inc_1 = 2
diag_1 = 0


for i in range(1, 1002):
    diag_1 += score_1
    score_1 += inc_1
    inc_1 += 2

score_2 = 1
inc_2 = 4
diag_2 = 0

for i in range(1, 1002):
    diag_2 += score_2
    score_2 += inc_2
    if i % 2 == 0:
        inc_2 += 4



print(diag_1 + diag_2 - 1)