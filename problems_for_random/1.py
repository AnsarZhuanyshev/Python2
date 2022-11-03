import random
from random import randint
n=0
while n!=3:
    x = random.randint(100,1000)
    if x%5==0:
        print(x)
        n+=1