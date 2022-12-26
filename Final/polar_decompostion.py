from sympy import *
import random
from math import *
import numpy as np
import math
def Polar():
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
    #print(Zero_matrix(matrix_size),"\n")

    #-------def for mul -------------
    def mat_mul(a_list, b_list):
        #------------zero matrix------------
        zero = Zero_matrix(matrix_size)
        #---------matrix mul--------
        for i in range(len(a_list)):
            for j in range(len(b_list[0])):
                for k in range(len(b_list)):
                    zero[i][j] += a_list[i][k] * b_list[k][j] 
        #-------matrix mul by z5 ----------
        return zero
    #print("This is multiplied matrix by Z5 " , mat_mul(a_list,a_list),"\n")

    #-------------sum--------------
    def mat_sum(a_list,b_list):
        #------------zero matrix------------
        zero = Zero_matrix(matrix_size)
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                zero[i][j] +=(a_list[i][j] + b_list[i][j])
        return zero
    #print("This is adition matrix " , mat_sum(a_list,a_list),"\n")

    #-------substraction --------
    def mat_substract(a_list,b_list):
        zero = Zero_matrix(matrix_size)
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                zero[i][j] +=(a_list[i][j] - b_list[i][j])
        return zero
    #print("This is subtraction matrix ",mat_substract(mat_mul(a_list,a_list),a_list),"\n")


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
    #print("This is transposed matrix ",transpos(a_list),"\n")

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
    print("This is our A_Transpose_to_A matrix" , A_transpose_to_A(a_list))

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
        A_transpose_A_sub_xI_list = mat_substract(A_transpose_to_A(a_list),xI_matrix(matrix_size))
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

    #-----------list with values ----------------
    Eigenvalues = Solving_polynomial_eq(a,b,c,d)
    print(Eigenvalues , " This is eigenvalues ", "\n")

    #-----------creating list with all matrix elements-------------
    def Matrices_for_Eigen_System(matrix_size):
        Eigenlist1 = []
        for k in Eigenvalues:
            for i in range(0,matrix_size):
                for j in range(0,matrix_size):
                    if i==j:
                        Eigenlist1.append(k)
                    else:
                        Eigenlist1.append(0)
        return Eigenlist1

    #-----------deviding into 3 lists----------------
    xI1_list = []
    xI2_list = []
    xI3_list = []
    if matrix_size ==2:
        for i in range(0,matrix_size*matrix_size):
            xI1_list.append(Matrices_for_Eigen_System(matrix_size)[i])
        for j in range(matrix_size*matrix_size,2*matrix_size*matrix_size):
            xI2_list.append(Matrices_for_Eigen_System(matrix_size)[j])
    elif matrix_size ==3:
        for i in range(0,matrix_size*matrix_size):
            xI1_list.append(Matrices_for_Eigen_System(matrix_size)[i])
        for j in range(matrix_size*matrix_size,2*matrix_size*matrix_size):
            xI2_list.append(Matrices_for_Eigen_System(matrix_size)[j])
        for k in range(2*matrix_size*matrix_size,3*matrix_size*matrix_size):
            xI3_list.append(Matrices_for_Eigen_System(matrix_size)[k])

    #-------------From 1x9 list create 3x3 matrix---------------
    def make_format(my_list):
        incorrect_format = np.array(my_list)
        correct_format = incorrect_format.reshape(matrix_size,matrix_size)
        return correct_format
    #print(make_format(xI1_list))
    #print(make_format(xI2_list))

    #--------------AtA-xI----------------
    if matrix_size == 3 :
        xI1_np = make_format(xI1_list)
        xI2_np = make_format(xI2_list)
        xI3_np = make_format(xI3_list)
        AtA_sub_xI1 = np.array(mat_substract(A_transpose_to_A(a_list),xI1_np))
        AtA_sub_xI2 = np.array(mat_substract(A_transpose_to_A(a_list),xI2_np))
        AtA_sub_xI3 = np.array(mat_substract(A_transpose_to_A(a_list),xI3_np))
    elif matrix_size ==2 :
        xI1_np = make_format(xI1_list)
        xI2_np = make_format(xI2_list)
        AtA_sub_xI1 = np.array(mat_substract(A_transpose_to_A(a_list),xI1_np))
        AtA_sub_xI2 = np.array(mat_substract(A_transpose_to_A(a_list),xI2_np))

    #-------------CEF of matrix AtA-xI-------------------
    def ref(mtx): 
        inverses = {1:1,2:3,3:2,4:4,0:1} 
        identityy = np.diagflat([1 for i in range(len(mtx))]) 
        for i in range(0, mtx.shape[0]): 
            j = 1 
            pivot = mtx[i][i] 
            while pivot == 0 and i + j < mtx.shape[0]: 
                identityy[[i, i + j]] = identityy[[i + j, i]] 
                mtx[[i, i + j]] = mtx[[i + j, i]] 
                j += 1 
                pivot = mtx[i][i] 
            if pivot == 0: 
                return [mtx%5,identityy%5] 
            row1 = mtx[i] 
            row2 = identityy[i] 
            identityy[i] = row2*inverses[pivot%5] 
            mtx[i] = row1*inverses[pivot%5] 
            for j in range(i + 1, mtx.shape[0]): 
                identityy[j] = identityy[j] - identityy[i] * mtx[j][i] 
                mtx[j] = mtx[j] - mtx[i] * mtx[j][i] 
        return mtx%5,identityy%5
    def cef(mtx): 
        new_mtx = mtx.T 
        arr = ref(new_mtx) 
        x,y = arr[0].T,arr[1].T 
        return x%5,y%5

    #-----------Eigenvectors ---------------------
    w , v = np.linalg.eig(A_transpose_to_A(a_list))
    print(v," Eigenvector matrix","\n")

    #----------Format for inverse -------------
    def format_for_inverse(mat,matrix_size):
        l = []
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                l.append(mat[i][j])
        return l
    v_format = format_for_inverse(v,matrix_size)

    #-------inverse for maatrices---------------
    def inverse_matrix(a):
        if matrix_size == 3:
            def determinant3(a_list):
                sum = a_list[0,0] * (a_list[1,1] * a_list[2,2] - a_list[1,2] * a_list[2,1]) - a_list[0,1] * (a_list[1,0] * a_list[2,2] - a_list[2,0] * a_list[1,2]) + a_list[0,2] * (a_list[1,0]*a_list[2,1] -a_list[2,0] * a_list[1,1])
                return sum
            def transpose(a):
                a1 = []
                for i in range(3):
                    for j in range(3):
                        a1.append(a[j,i])
                return a1
            def step3(a):
                a = np.array(a)
                a = a.reshape(3,3)
                ans =[]
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=0 and j !=0:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=0 and j !=1:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=0 and j !=2:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=1 and j !=0:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=1 and j !=1:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=1 and j !=2:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=2 and j !=0:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=2 and j !=1:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                for i in range(3):
                    for j in range(3):
                        if i!=2 and j !=2:
                            an.append(a[i,j])
                ans.append(an[0] * an[3] - an[1] * an[2])
                an = []
                '''ans.append(a[1,1] * a[2,2] - a[1,2] * a[2,1])
                ans.append(a[1,0] * a[2,2] - a[1,2] * a[2,0])
                ans.append(a[1,0] * a[2,1] - a[1,1] * a[2,1])'''
                return ans
            a = np.array(a)
            a = a.reshape(3,3)
            detA=determinant3(a)
            tran = transpose(a)
            mat1 = step3(tran)
            for i in range(len(mat1)):
                if i%2 ==1:
                    mat1[i] = -1*mat1[i]
            x = 1/detA
            for i in range(9):
                mat1[i] = x * mat1[i]
                y = str(mat1[i])
                if y[-2:] == '.0':
                    mat1[i] = int(mat1[i]) 
            return (mat1)
        elif matrix_size == 2 :
            def determinant2(a_list):
                a_list = np.array(a)
                a_list = a_list.reshape(2,2)
                sum = (a_list[0,0] * a_list[1,1] - a_list[0,1] * a_list[1,0])
                return sum
            def transpose(a):
                a1 = []
                a1.append(a[3])
                a1.append(-1*a[1])
                a1.append(-1*a[2])
                a1.append(a[0])
                return a1
            detA = determinant2(a)
            mat1 = transpose(a)
            x = 1/detA
            for i in range(4):
                mat1[i] = x * mat1[i]
                y = str(mat1[i])
                if y[-2:] == '.0':
                    mat1[i] = int(mat1[i]) 
            return (mat1)
    v_invers = make_format(inverse_matrix(v_format))
    print(v_invers," This is Eigenvector inverse matrix" , "\n")

    #----------Diagonal matrix------------
    def Diagonal_matrix(matrix_size):
        zer0 = Zero_matrix(matrix_size)
        l = Eigenvalues
        if matrix_size == 3:
            zer0[0][0] += (ceil(l[0]*100)/100)**0.5
            zer0[1][1] += (ceil(l[1]*100)/100)**0.5
            zer0[2][2] += (ceil(l[2]*100)/100)**0.5
        elif matrix_size == 2:
            zer0[0][0] += (ceil(l[0]*100)/100)**0.5
            zer0[1][1] += (ceil(l[1]*100)/100)**0.5
        return zer0
    Square_diagonal_list = Diagonal_matrix(matrix_size)
    Square_diagonal_matrix = np.array(Square_diagonal_list)

    print(Square_diagonal_matrix, " Square root diagonal matrix","\n")


    #--------------- S = V D V^-1---------------
    S_list = mat_mul(mat_mul(v,Square_diagonal_matrix),v_invers)
    S_inverse = inverse_matrix(format_for_inverse(make_format(S_list),matrix_size))
    S_inverse_matrix = np.array(S_inverse).reshape(matrix_size,matrix_size)
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            S_inverse_matrix[i][j] = (S_inverse_matrix[i][j]) 
    print(S_inverse_matrix , " S inverse matrix","\n")

    #------------Q matrix -----------
    Q = mat_mul(a_list,S_inverse_matrix)
    print(np.array(Q) , " Q matrix","\n")


    print(np.array(mat_mul(Q,S_list)), " A matrix", "\n" )
print(Polar())