import math
from sympy import sympify
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
#y' = 2*y-x, y(1) = 0, x (= [1;2,2], h = 0.3,  0.5*x+0.25-0.75*exp(2*x-2)
func = "y'=7-x*y"
a,b,h,dta,data = -2,0,0.5,"y(-2)=0",""
for i in dta:
    if i in "0123456789":
        data+=i
    else:
        data+=" "
data1 = data.split()
x0,y0,fxy,exact = float(data1[0]),float(data1[1]),sympify(func.split("=")[1]),'0.5*x+0.25-0.75*exp(2*x-2)'
f = sympify(exact)
def subsxy(fxy,x,y):
    expr = fxy.subs("x",x)
    expr = expr.subs("y",y) 
    return expr
def euler(fxy,a,b,h,x0,y0):
    n = int((((b-a)/h)))
    arr = [[] for i in range(n+1)]
    arr[0] = [y0,x0]
    for i in range(n):
        y = arr[i][0]+h*(subsxy(fxy,arr[i][1],arr[i][0]))
        x = arr[i][1]+h
        arr[i+1] = [y,x]
    return arr
def heun(fxy,a,b,h,x0,y0):
    n = int((((b-a)/h)))
    arr = [[] for i in range(n+1)]
    arr[0] = [y0,x0]
    for i in range(n):
        x = arr[i][1]+h
        y = arr[i][0]+h*(subsxy(fxy,arr[i][1],arr[i][0])+subsxy(fxy,x,arr[i][0]+h*subsxy(fxy,arr[i][1],arr[i][0])))/2
        arr[i+1] = [y,x]
    return arr
x = [-2,-1.5,-1,-0.5,0]
y = [0,3.5,12.3,22.93,31.481]
xyeuler = euler(fxy,a,b,h,x0,y0)
x1,y1 = [-2,-1.5,-1,-0.5,0],[0,3.5,9.625,17.93,25.92]
xyhein = heun(fxy,a,b,h,x0,y0)
x2,y2 = [-2,-1.5,-1,-0.5,0],[0,4.82,13.09,22.76,29.111]
plt.plot(x,y,label = "Exact solution",color = 'green')
plt.plot(x1,y1,label = "Euler's approximation",marker = 'o',color = "blue")
plt.plot(x2,y2,label = "Heyn's approximation",marker = 'o',color = 'red')
plt.grid(True)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Numerical solutuion of first order differential equation,red graph for Heyn's,blue for Euler's,green is graph of exact solution")
plt.show()