from sympy import *
import random
import math
import numpy as np
#------------ A = Q * S ------------

#--------size for matrix--------------
matrix_size = int(input("What is the size of matrix?"))

#----------initial matrix-------------
a_list = []
a_str = []
for i in range(0,matrix_size):
    for j in range(0,matrix_size):
        a_str.append(random.randint(0,4))
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
print(Zero_matrix(matrix_size),"\n")

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
            el_by_z5 = el % 5
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

#-------substraction--------
def mat_substract(a_list,b_list):
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
            zero[i][j] +=(a_list[i][j] - b_list[i][j])%5
    return zero
#print("This is subtraction matrix ",mat_substract(a_list,b_list),"\n")

#-------substraction in R --------
def mat_substract_in_R(a_list,b_list):
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
            zero[i][j] +=(a_list[i][j] - b_list[i][j])
    return zero
#print("This is subtraction matrix ",mat_substract(a_list,b_list),"\n")

#--------transpose------------------
def transpos(a_list):
    str_transpose = []
    m_transpose = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            str_transpose.append(a_list[j][i])
        m_transpose.append(str_transpose)
        str_transpose = []
    return m_transpose
#print("This is transposed matrix ",transpose(a_list),"\n")

#-----------determinant equation------------
def determinant(a_list):
    sum = 0 
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            if matrix_size == 2:
                sum = a_list[0][0] * a_list[1][1] - a_list[0][1] * a_list[1][0]
            elif matrix_size == 3 :
                sum = a_list[0][0] * (a_list[1][1] * a_list[2][2] - a_list[1][2] * a_list[2][1]) - a_list[0][1] * (a_list[1][0] * a_list[2][2] - a_list[2][0] * a_list[1][2]) + a_list[0][2] * (a_list[1][0]*a_list[2][1] -a_list[2][0] * a_list[1][1])
            elif matrix_size == 4:
                sum = a_list[0][0] * (a_list[1][1] * (a_list[2][2] * a_list[3][3] - a_list[2][3] * a_list[3][2]) - a_list[1][2] * (a_list[2][1] * a_list[3][3] - a_list[3][1] * a_list[2][3]) + a_list[1][3] * (a_list[2][1]*a_list[3][2] -a_list[3][1] * a_list[2][2]))  - a_list[0][1] * (a_list[1][0] * (a_list[2][2] * a_list[3][3] - a_list[2][3] * a_list[3][2]) - a_list[1][2] * (a_list[2][0] * a_list[3][3] - a_list[3][0] * a_list[2][3]) + a_list[1][3] * (a_list[2][0]*a_list[3][2] -a_list[3][0] * a_list[2][2]))+ a_list[0][2] * (a_list[1][0] * (a_list[2][1] * a_list[3][3] - a_list[2][3] * a_list[3][1]) - a_list[1][1] * (a_list[2][0] * a_list[3][3] - a_list[3][0] * a_list[2][3]) + a_list[1][3] * (a_list[2][0]*a_list[3][1] -a_list[3][0] * a_list[2][1]))- a_list[0][3] * (a_list[1][0] * (a_list[2][1] * a_list[3][2] - a_list[2][2] * a_list[3][1]) - a_list[1][1] * (a_list[2][0] * a_list[3][2] - a_list[3][0] * a_list[2][2]) + a_list[1][2] * (a_list[2][0]*a_list[3][1] -a_list[3][0] * a_list[2][1]))
    return sum
#print("This is determinant " , determinant(a_list),"\n")

#-----------A_transpose_A--------------
def A_transpose_to_A(a_list):
    A_transpose_A_list = mat_mul(transpos(a_list),a_list)
    return A_transpose_A_list
#print("This is our A_Transpose_to_A matrix" , A_transpose_to_A(a_list))

#---------xI matrix-------------
def xI_matrix(matrix_size):
    x = var("x")
    xI_list = []
    xI_str = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            if i==j:
                xI_str.append(x)
            else:
                xI_str.append(0)
        xI_list.append(xI_str)
        xI_str = []
    return xI_list
#print("This is xI matrix " , xI_matrix(matrix_size))

#-----------A_transpose_A - xI --------------
def A_transpose_A_sub_xI(a_list,matrix_size):
    A_transpose_A_sub_xI_list = mat_substract_in_R(A_transpose_to_A(a_list),xI_matrix(matrix_size))
    return A_transpose_A_sub_xI_list
#print(A_transpose_A_sub_xI(a_list,matrix_size),"\n")

#--------Polynomial equation---------------
def Polynomial_equation(a_list,matrix_size):
    Eqat = determinant(A_transpose_A_sub_xI(a_list,matrix_size))
    Eqqq = expand(Eqat)
    return Eqqq
print(Polynomial_equation(a_list,matrix_size),"\n")

a = int(input("Please input coefficient of third degree :  "))
b = int(input("Please input coefficient of second degree :  "))
c = int(input("Please input coefficient of first degree :  "))
d = int(input("Please input coefficient of zero degree :  "))

#----------Solving polynom eq--------------
def Solving_polynomial_eq(a, b, c, d):
    if (a == 0 and b == 0):                     
        return np.array([(-d * 1.0) / c])                 
    elif (a == 0):                              
        D = c * c - 4.0 * b * d                       
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)
        return np.array([x1, x2])               

    f = findF(a, b, c)                          
    g = findG(a, b, c, d)                       
    h = findH(g, f)                            

    if f == 0 and g == 0 and h == 0:            
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return np.array([x, x, x])              

    elif h <= 0:                                
        i = math.sqrt(((g ** 2.0) / 4.0) - h)   
        j = i ** (1 / 3.0)                     
        k = math.acos(-(g / (2 * i)))           
        L = j * -1                              
        M = math.cos(k / 3.0)                 
        N = math.sqrt(3) * math.sin(k / 3.0)    
        P = (b / (3.0 * a)) * -1               
        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        return np.array([x1, x2, x3])           

    elif h > 0:                              
        R = -(g / 2.0) + math.sqrt(h)          
        if R >= 0:
            S = R ** (1 / 3.0)                 
        else:
            S = (-R) ** (1 / 3.0) * -1         
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))                
        else:
            U = ((-T) ** (1 / 3.0)) * -1        
        #--------two roots are complex and one real 
        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j

        return np.array([x1, x2, x3])           
#-------------finding first root helper function--------------
def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0
#-------------finding second root helper function--------------
def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a **2.0)) + (27.0 * d / a)) /27.0
#-------------finding third root helper function--------------
def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)
#print(Solving_polynomial_eq(a,b,c,d))

#-------------take Values by Z5--------------
def Eigenvalues_by_z5():
    eigen_values_list = Solving_polynomial_eq(a,b,c,d)
    eigen_values_list_by_z5 = []
    for i in eigen_values_list:
        eigenValue = (round(i) * 36 ) % 5 
        eigen_values_list_by_z5.append(eigenValue)
    return eigen_values_list_by_z5
print(Eigenvalues_by_z5())

#-----------creating matrices-------------
def Matrices_for_Eigen_System(matrix_size):
    EigenMatrix1 = []
    for k in Eigenvalues_by_z5():
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                if i==j:
                    EigenMatrix1.append(k)
                else:
                    EigenMatrix1.append(0)
    return EigenMatrix1
print(Matrices_for_Eigen_System(matrix_size))