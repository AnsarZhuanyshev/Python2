import random 
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