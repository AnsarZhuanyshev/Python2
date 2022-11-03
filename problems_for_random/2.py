import random
from random import randint

n = 0 

my_list = []
while n!=100:
    x= random.randint(10,1000)
    if x not in my_list:
        my_list.append(x)
        n+=1    

winners_list = random.choices(my_list , k=2)

print(winners_list)