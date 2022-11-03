import random 
from random import randint

l = int(input("input the lenth of string"))

cnt = 0 

my_list =[]

s=''

while cnt!=l:
    specific_char = chr(random.randint(ord('!'), ord('/')))
    specific_char2 = chr(random.randint(ord(':'), ord('@')))
    if specific_char2 not in my_list:
        my_list.append(specific_char2)
        cnt+=1
    elif specific_char not in my_list:
        my_list.append(specific_char)
        cnt+=1

for i in my_list:
    s+=str(i)
print(s)