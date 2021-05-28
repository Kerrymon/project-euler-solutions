""" Euler Problem #5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

i = 21

while True:
     score = 0
     for delitel in range(1, 21):
         if i % delitel == 0:
             score += 1
             if score == 19:
                 print(i, "Число, которое делится на все числа от 1 до 20")
                 break

         else:
             break

     i += 1
