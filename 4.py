""" Euler Problem #4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

# брутфорсом проходимся по шестизначным числам
for sixdigitnumber in range(100000, 1000000):
    # разделяем по цифрам в лист
    listfdn = list(str(sixdigitnumber))
    # если число палиндром
    if (listfdn[0] == listfdn[5]) and (listfdn[1] == listfdn[4]) and (listfdn[2] == listfdn[3]):
        # ищем делитель без остатка от 100 до 999
        for threedigitnumber in range(100, 1000):
            # проверяем верен ли делитель и то, что остаток будет трехзначным
            if sixdigitnumber % threedigitnumber == 0 and len(list(str(int(sixdigitnumber/threedigitnumber)))) == 3:
                # записываем остаток
                secondnum = int(sixdigitnumber / threedigitnumber)
                # выводим число и его два делителя
                print("Число", sixdigitnumber, " делится на числа ", threedigitnumber," и ", secondnum)
