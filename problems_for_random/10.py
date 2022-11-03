import string 
import random 
from random import randint 

cnt = 0 
cnt1 = 0

my_list = []

my_list1 = random.choices(string.digits , k=4)


while cnt !=6 :
    x = random.choice(string.ascii_letters + string.digits)
    if x not in my_list:
        my_list.append(x)
        cnt += 1

overall_list = []

overall_cnt = 0

ans_list = []

for i in my_list:
    overall_list.append(i)
for j in my_list1:
    overall_list.append(j)

while overall_cnt !=10:
    el = random.choice(my_list + my_list1)
    if el not in ans_list:
        ans_list.append(el)
        overall_cnt+=1

s = ''

for i in ans_list:
    s += str(i)

print(s)