import random 
from random import randint 

s = str(input())

my_list = []

l = len(s)

for i in s:
    my_list.append(i)

ans = random.choice(my_list)

print(ans)