""" Euler Problem #5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

from datetime import datetime


start_time = datetime.now()
i = 21
while True:
     score = 0
     for delitel in range(1, 21):
         if i % delitel == 0:
             score += 1
             if score == 20:
                 print(i, "Число, которое делится на все числа от 1 до 20")
                 break
         else:
             break

     i += 1
     if score == 20:
         break
end_time = datetime.now()
# Works in two minutes, need some optimization
print('Duration: {}'.format(end_time - start_time))