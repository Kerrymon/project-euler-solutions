"""By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family."""

from math import sqrt
from itertools import combinations, permutations, product
import copy


def prime(number):
    if number == 1:
        return False
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return True
    return False

def factorial(number):
    fact_sum = 1
    if number == 0 or number == 1:
        return 1
    for i in range(1, number+1):
        fact_sum *= i

    return fact_sum



if __name__ == '__main__':
    """TESTING prime Function
    lst_prime = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 21, 20, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40]
    answers_test_prime = []
    answers_test_prime.extend([False for i in range(18)])
    answers_test_prime.extend([True for i in range(27)])
    for lst_test_prime_number, answer_bool in zip(lst_prime, answers_test_prime):
        if prime(lst_test_prime_number) == answer_bool:
            print("TEST PASSED!")
        else:
            print("TEST FAILED!")
    """
    for i in range(0, 1000):
        n = [int(x) for x in str(i)]
        changed = copy.deepcopy(n)
        for i in range(0, len(n)-1):
            for j in range(1, len(n)):
                if i>=j:
                    continue
                changed[i] = '*'
                changed[j] = '*'
               # print(changed)
                prime_score = 0
                for k in range(0, 10):
                    new_digit_lst = [k if x == '*' else x for x in changed]
                    new_digit = int(''.join(str(i) for i in new_digit_lst))
                    if prime(new_digit) == True:
                        prime_score += 1

                if prime_score == 7:
                    print(changed)



                    print(new_digit)


                changed = copy.deepcopy(n)



