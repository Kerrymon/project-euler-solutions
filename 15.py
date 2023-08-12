"""Euler Problem #15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""

def fact(num):
    factorial = 1
    while num != 1:
        factorial *= num
        num -= 1
    if num == 0:
        return 1
    return factorial

for i in range(1, 21):
    if i == 20:
         print(int(fact(2*i)/(fact(i)*fact(i))))