""" Euler Problem #3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from functools import reduce

largenumber = 600851475143
# число которое будет хранить в себе остаток от деления largenumber на bfnumber
newlargenumber = 0
# список, который будет хранить в себе все простые делители числа largenumber
primearr = []
# счетчик, который будет использоваться для перебора
bfnumber = 1
score = 0
while newlargenumber != 1:
    bfnumber += 1
    # если число bfnumber является делителем largenumber
    if largenumber % bfnumber == 0:
        # перебираем диапозон чисел от 2 до найденого делителя, чтобы проверить его на простоту
        for delitel in range(2, bfnumber + 1):
            # если число не простое, то прерываем цикл
            if bfnumber % delitel == 0 and not bfnumber == delitel:
                break
            # если число простое
            else:
                if bfnumber == delitel:
                    # добавляем это число в наш список простых чисел и прерываем цикл
                    primearr.append(bfnumber)
                    print(bfnumber, "- простое число")
                    break
        # перемножаем весь список простых чисел
        multiprime = reduce(lambda x, y: x*y, primearr)
        # делим largenumber на перемноженный список и записываем в переменную newlargenumber
        newlargenumber = int(largenumber / multiprime)
        print("новое большое число - ", newlargenumber)

# выводим максимальное значение из списка простых чисел как ответ
print("\nСамое большое простое число -", max(primearr))