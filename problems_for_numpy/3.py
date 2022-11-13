import numpy as np 
arr1 = np.array([1,0,1,0,0,0,0,1,1,1,1])
arr2 = np.array([1,0,1,0,0,0,0,1,1,1,1])

l = len(arr2)

cnt = 0 

for i in range (0,l):
    if arr2[i]==0:
        arr2[i]=1
    elif arr2[i]==1:
        arr2[i]=0

if arr1[0]==1:
    for i in range(0,l):
        if arr2[i]==1:
            cnt +=1 
            if arr2[i]==0:
                arr2[i]=1
            elif arr2[i]==1:
                arr2[i]=0
            
print("Freed prisoners" , cnt)