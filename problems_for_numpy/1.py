import numpy as np #### use alias np instead of numpy 

arr1 = np.array([[1, 2, 3, 6 ],
                [4, 5, 6, 13],  
                [7, 8, 9, 24],    
                [12,15,18,45]])

for i in range(0,4):
    sum_of_el =0
    for j in range(0,3):
        sum_of_el += arr1[i,j]
    if sum_of_el != arr1[i,3]:
        row = i
        ###print(arr1[i,:]) all el in incorrect row 

for j in range(0,4):
    sum_of_el = 0
    for i in range(0,3):
        sum_of_el += arr1[i,j]
    if sum_of_el != arr1[3,j]:
        col = j
        ###print(arr1[:,j]) all elements in column
print(arr1[row , col]," is incorrect in " ,row,"-row and ",col,"-column" )

arr1[arr1 == arr1[row,col]] = 0

a=0
for j in range(0,3):
    a += arr1[row , j]
    #arr1[arr1 == arr1[row,col]] = arr1[row,3]
b= arr1[row,3] - a
arr1[arr1 == arr1[row,col]] = b 

print("replace it with , ",abs(b))
