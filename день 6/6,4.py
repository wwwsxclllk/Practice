from collections import Counter
from random import randint

c1 = []
c2 = []

for i in range(randint(0,10)):
    c1.append(str(randint(0,20)))
    c2.append(str(randint(0,20)))
    if int(c1[i]) == int(c2[i]):
        print(c1[i], " : ", c2[i])
