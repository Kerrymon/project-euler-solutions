"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?"""

from collections import Counter
from datetime import datetime

start_time = datetime.now()

lstofperimeters = []
for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a + b + c > 1000:
                break
            if a + b > c and a*a + b*b == c*c:
                lstofperimeters.append(a+b+c)






print(Counter(lstofperimeters))

end_time = datetime.now()

print("Duration   -", end_time - start_time)

