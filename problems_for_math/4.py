import math 
import itertools 

def all_perm(n): 
    global all_perm 
    numbers = [] 
    cnt = 0
    while cnt != n: 
        numbers.append(cnt) 
        cnt += 1
    all_perm = [p for p in itertools.product(numbers, repeat=n)] 
    return all_perm 
 
def number_of_repeat(a): 
    cnt = 0 
    all_cnt = [] 
    for i in range(len(a) - 1): 
        
        if a[i] != a[i+1]: 
            all_cnt.append(cnt + 1) 
            cnt = 0

        elif a[i] == a[i+1]: 
            cnt += 1 
            if i == len(a) - 2: 
                all_cnt.append(cnt + 1)     

    return max(all_cnt) 
 
def all(): 
    n = int(input("n = ")) 
    all_perm(n) 
    cnt = 0 
    for seq in all_perm: 
        cnt += number_of_repeat(seq) 
    print(cnt) 
 
all()