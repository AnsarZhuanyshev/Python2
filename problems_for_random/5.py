import string 
import random 
from random import randint 

list_with_upper = random.choices(string.ascii_uppercase,k=2)
list_with_digit = random.choice(string.digits)
list_with_symbol = random.choices(string.punctuation)

list_mix = random.choices(string.digits + string.ascii_letters + string.punctuation ,k=6)

my_list = []
my_list2 =[]
for i in list_with_upper:
    my_list.append(i)
for i in list_with_digit:
    my_list.append(i)
for i in list_with_symbol:
    my_list.append(i)
for i in list_mix:
    my_list.append(i)

cnt = 0 


while cnt!=10:
    x = random.choice(my_list)
    if x not in my_list2:
        my_list2.append(x)    
        cnt+=1

s=''

for i in my_list2:
    s += str(i)

print(s)