import random
from random import randint

list = []

for i in range(10):
    list.append(randint(-10,10))
print(list)
print(sorted(list))