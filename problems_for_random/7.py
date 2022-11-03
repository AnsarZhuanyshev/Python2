import random 
from random import randint 

cnt = 0 

while cnt!=5:
    a = random.randint(0,6)
    b = random.randint(0,6)

    if a == b:
        print(a,b)
        cnt +=1
    else:
        continue

