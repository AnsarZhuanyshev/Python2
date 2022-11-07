import numpy as np 

arr = np.array([[1,2,3,4,5,3,2,4,3,3],
                [2,3,5,5,6,7,7,8,7,6],
                [3,4,6,6,7,8,9,9,9,9],
                [1,2,3,4,5,6,6,5,5,5]])

l = len(arr[:,0])
l1 = len(arr[0,:])
cnt = 0
####print(l) number of rows
####print(l1) number of columns
#------------------for all previously bigger numbers-----------------
for i in range(l-1):
    for j in range(l1):
        if arr[i,j]>arr[i+1,j]:
            cnt += 1
        else:
            cnt += 0
if cnt==0:
    print("TRUE")
else:
    print("FALSE")

