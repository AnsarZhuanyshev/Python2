import random 
import numpy as np
def Mat_Operations():
    #----------size-------------
    matrix_size = int(input())

    #----------first matrix-------------
    a_list = []
    a_str = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            a_str.append(random.randint(0,4))
        a_list.append(a_str)
        a_str = []
    print("This is first matrix " , a_list , "\n")

    #-----------second matrix------------
    b_list = []
    b_str = []
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            b_str.append(random.randint(0,4))
        b_list.append(b_str)
        b_str = []
    print("This is second matrix " , b_list, "\n")

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
    print("This is multiplied matrix by Z5 " , mat_mul(a_list,b_list),"\n")

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
    print("This is adition matrix " , mat_sum(a_list,b_list),"\n")

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
    print("This is subtraction matrix ",mat_substract(a_list,b_list),"\n")

    #--------transpose------------------
    def transpose(a_list):
        str_transpose = []
        m_transpose = []
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                str_transpose.append(a_list[j][i])
            m_transpose.append(str_transpose)
            str_transpose = []
        return m_transpose
    print("This is transposed matrix ",transpose(a_list),"\n")

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
    print("This is determinant " , determinant(a_list),"\n")

    #----------Format for inverse -------------
    def format_for_inverse(mat,matrix_size):
        l = []
        for i in range(0,matrix_size):
            for j in range(0,matrix_size):
                l.append(mat[i][j])
        return l
    i_format = format_for_inverse(a_list,matrix_size)

    def make_format(my_list):
        incorrect_format = np.array(my_list)
        correct_format = incorrect_format.reshape(matrix_size,matrix_size)
        return correct_format
    #-----------inverse -------------------
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

    print("This is the inverse matrix of A " ,"\n", make_format(inverse_matrix(i_format)))

print(Mat_Operations())