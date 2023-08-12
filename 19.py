"""Euler Problem #19:
You are given the following information, but you may prefer to do some research for yourself.

1) 1 Jan 1900 was a Monday.
2) Thirty days has September,
April, June and November.
 All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
3)A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""


days = 1
score = 0
visok = 0
days_1 = 1

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while days_1 <= 36524:
    visok += 1
    if visok != 0 and visok % 4 == 0:
        months[1] = months[1] + 1
        for i in range(12):
            days_1 += months[i]
            days = days_1
            while days >= 7:
                days -= 7
            if days % 6 == 0 and days != 0:
                score += 1
        months[1] = months[1] - 1
    else:
        for i in range(12):
            days_1 += months[i]
            days = days_1
            while days >= 7:
                days -= 7
            if days % 6 == 0 and days != 0:
                score += 1



print(score)
