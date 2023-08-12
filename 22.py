"""Euler Problem #22:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""


names = open("p022_names.txt", "r")
namestr = names.read()

lstnames = list(namestr.split(","))

lstnames.sort()

score = 0

def convert(string):
    score = 0
    li = []
    li[:] = string
    for ordinary in li:
        value = ord(ordinary) - 64
        if value > 0:
            score += value
    return score

i = 1
final = 0
for n in lstnames:
   final +=  convert(n)*i
   i += 1

print(final)