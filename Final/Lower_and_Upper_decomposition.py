from sympy import *
import random
import math
import numpy as np

#--------size for matrix--------------
matrix_size = int(input("What is the size of matrix?"))

#----------initial matrix-------------
a_list = []
a_str = []
for i in range(0,matrix_size):
    for j in range(0,matrix_size):
        a_str.append(random.randint(1,4))
    a_list.append(a_str)
    a_str = []
print("This is first matrix " , a_list , "\n")

#--------Zero matrix -----------
def Zero_matrix(matrix_size):
    zero_str = []
    zero_list = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            zero_str.append(0)
        zero_list.append(zero_str)
        zero_str = []
    return zero_list
#print(Zero_matrix(matrix_size),"\n")

#-----------b vector --------------------
b_vector = []
for i in range(0,matrix_size):
    b_vector.append(random.randint(0,4))
print("This is main vector" , b_vector ,"\n")

#-------def for mul -------------
def mat_mul(a_list, b_list):
    #------------zero matrix------------
    zero_str = []
    zero = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            zero_str.append(0)
        zero.append(zero_str)
        zero_str=[]
    #---------matrix mul--------
    for i in range(len(a_list)):
        for j in range(len(b_list[0])):
            for k in range(len(b_list)):
                zero[i][j] += a_list[i][k] * b_list[k][j] 
    #-------matrix mul by z5 ----------
    mul_str = []
    mul_list = []
    for el_str in zero:
        for el in el_str:
            el_by_z5 = el 
            mul_str.append(el_by_z5)
        mul_list.append(mul_str)
        mul_str = []
    return mul_list
#print("This is multiplied matrix by Z5 " , mat_mul(a_list,b_list),"\n")

#-------------sum--------------
def mat_sum(a_list,b_list):
    #------------zero matrix------------
    zero_str = []
    zero = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            zero_str.append(0)
        zero.append(zero_str)
        zero_str=[]
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            zero[i][j] +=(a_list[i][j] + b_list[i][j]) % 5
    return zero
#print("This is adition matrix " , mat_sum(a_list,b_list),"\n")

#--------------with unknowns --------------------
def L_unknown(matrix_size):
    l_mat = Zero_matrix(matrix_size)
    if matrix_size == 2:  
        l1 = var("l1")
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i==j:
                    l_mat[i][j] = 1
                elif i<j :
                    l_mat[i][j] = 0 
                l_mat[1][0] = l1
    elif matrix_size == 3:
        l1=var("l1")
        l2=var("l2")
        l3=var("l3")
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if  i<j:
                    l_mat[i][j] =0
                elif i==j:
                    l_mat[i][j] =1
                l_mat[1][0] = l1
                l_mat[2][0] = l2
                l_mat[2][1] = l3
    return l_mat

#------------with unknowns ---------------
def U_unknown(matrix_size):
    u_mat = Zero_matrix(matrix_size)
    if matrix_size == 2:  
        u1 = var("u1")
        u2 = var("u2")
        u3 = var("u3")
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i>j:
                    u_mat[i][j] = 0 
                u_mat[0][0] = u1
                u_mat[0][1] = u2 
                u_mat[1][1] = u3
    if matrix_size == 3:  
        u1 = var("u1")
        u2 = var("u2")
        u3 = var("u3")
        u4 = var("u4")
        u5 = var("u5")
        u6 = var("u6")
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i>j:
                    u_mat[i][j] = 0 
                u_mat[0][0] = u1
                u_mat[0][1] = u2 
                u_mat[0][2] = u3
                u_mat[1][1] = u4
                u_mat[1][2] = u5
                u_mat[2][2] = u6
    return u_mat
print(L_unknown(matrix_size),"\n")
print(U_unknown(matrix_size),"\n")

#--------------- LU matrix with unknowns --------------
LU = mat_mul(L_unknown(matrix_size),U_unknown(matrix_size))
print(LU,"\n")
#---------U matrix variables---------------
u1 = var("u1")
u2 = var("u2")
u3 = var("u3")
u4 = var("u4")
u5 = var("u5")
u6 = var("u6")
#--------L matrix variables----------------
l1 = var("l1")
l2 = var("l2")
l3 = var("l3")

#------------finding values of unknowns ------------
def Finding_unknowns(matrix_size):
    if matrix_size ==2 :
        expr1 = LU[0][0] - a_list[0][0]
        expr2 = LU[1][0] - a_list[1][0]
        expr3 = LU[0][1] - a_list[0][1]
        expr4 = LU[1][1] - a_list[1][1]
        EQ = solve((expr1,expr2,expr3,expr4),(u1,u2,u3,l1))

    if matrix_size == 3 :
        expr1 = LU[0][0] - a_list[0][0]
        expr2 = LU[0][1] - a_list[0][1]
        expr3 = LU[0][2] - a_list[0][2]
        expr4 = LU[1][0] - a_list[1][0]
        expr5 = LU[1][1] - a_list[1][1]
        expr6 = LU[1][2] - a_list[1][2]
        expr7 = LU[2][0] - a_list[2][0]
        expr8 = LU[2][1] - a_list[2][1]
        expr9 = LU[2][2] - a_list[2][2]
        EQ = solve((expr1,expr2,expr3,expr4,expr5,expr6,expr7,expr8,expr9),(u1,u2,u3,u4,u5,u6,l1,l2,l3))
    return EQ
print(Finding_unknowns(matrix_size),"\n")

#--------------U matrix---------------------
def U(matrix_size):
    u_mat = Zero_matrix(matrix_size)
    if matrix_size == 2:  
        u_mat[0][0] =   float(input("Please input first number from list   "))
        u_mat[0][1] =   float(input("Please input second number from list   "))
        u_mat[1][1] =   float(input("Please input third number from list   "))
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i>j:
                    u_mat[i][j] = 0 
    if matrix_size == 3:  
        u_mat[0][0] = float(input("Please input first number from list   "))
        u_mat[0][1] = float(input("Please input second number from list   "))
        u_mat[0][2] = float(input("Please input third number from list   "))
        u_mat[1][1] = float(input("Please input fourth number from list   "))
        u_mat[1][2] = float(input("Please input fifth number from list   "))
        u_mat[2][2] = float(input("Please input sixth number from list   "))
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i>j:
                    u_mat[i][j] = 0 
    return u_mat
U_mat = U(matrix_size)
print(U_mat,"\n")
#---------------L matrix------------------
def L(matrix_size):
    l_mat = Zero_matrix(matrix_size)
    if matrix_size == 2:  
        l_mat[1][0] = float(input("Please input fourth number from list   "))
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i==j:
                    l_mat[i][j] = 1
                elif i<j :
                    l_mat[i][j] = 0 
    elif matrix_size == 3:
        l_mat[1][0] = float(input("Please input seventh number from list   "))
        l_mat[2][0] = float(input("Please input eights number from list   "))
        l_mat[2][1] = float(input("Please input ninth number from list   "))
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if  i<j:
                    l_mat[i][j] =0
                elif i==j:
                    l_mat[i][j] =1
    return l_mat
L_mat = L(matrix_size)
print(L_mat,"\n")

print(mat_mul(L_mat,U_mat),"\n")
#------------ L * Y vector = B vector -----------
Y_vector = np.linalg.solve(L_mat,b_vector)
print(Y_vector,"\n")

#----------- U * X vector   =  Y vector ----------
X_vector = np.linalg.solve(U_mat,Y_vector)
print("This is the solution of LU decomposition   -  " , X_vector , "\n")