import math
import numpy as np
a = int(input())
b = int(input())
c = int(input())
d = int(input())
def solve(a, b, c, d):
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
        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j
        return np.array([x1, x2, x3])           
def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0
def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a **2.0)) + (27.0 * d / a)) /27.0
def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)
print(solve(a,b,c,d))