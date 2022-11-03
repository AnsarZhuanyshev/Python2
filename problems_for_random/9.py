import random 
from random import randint 

l = int(input("input the lenth of the string : "))

cnt = 0 

my_list = []

s =''

while cnt != l :
    x = chr(random.randint(ord('!') , ord('}')))
    if x not in my_list:
        my_list.append(x)
        cnt +=1 

for i in my_list:
    s += str(i)

print (s)