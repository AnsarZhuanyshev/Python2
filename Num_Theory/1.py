#------------11 variant---------------
#-------------integral of x**2 + sqrt(x+2) - 1 dx ------ n=8--------
import math
from sympy import *
#------------condition-----------
x = var("x")
a = -2
b = 2
n = 8
func = x**2+(x+2)**(1/2)-1
#-------------------expr is our readiable part of function ----------
expr = sympify(func)
#-----it is computed exact solution of our integral--------
def exact_solution(expr,a,b):
    integral = integrate(expr,x)###intedrate by dx
    defined_integral = integral.subs(x,b)-integral.subs(x,a)###use limits 
    return defined_integral####return answer
#-------midpoint rule
def midpoint(expr,a,b,n):# our function by limits and number of steps 
    h = (b-a)/n#### formula for our steps 
    cnt = 0 ## counter 
    for i in range(n):#### circle 
        mid_point = (a+h/2)+i*h### while circle is working 
        if not math.isnan(expr.subs(x,mid_point)): ### check for input if it is not a not number (if it is number)
            cnt  += expr.subs(x,mid_point)### sum it to the counter which is sum of functions 
    return h*cnt #### return overall solution for midpoint 
#------------simpsons rule --------------
def simpson(expr,a,b,n):#### our function by steps and limits 
    cnt,h = expr.subs(x,a)+expr.subs(x,b),(b-a)/n### substitutions and sum to counter 
    point,k = a+h,1### increase the step 
    while point<b:##### while it is not equal to the limit 
        if k == 1:#### if place is odd 
            if not math.isnan(expr.subs(x,point)):
                cnt +=4*expr.subs(x,point)
            k=0
        elif k==0:### if even 
            if not math.isnan(expr.subs(x,point)):
                cnt +=2*expr.subs(x,point)
            k=1
        point+=h
    return h*cnt/3### main formula 

print("Result obtained by midpoint method: ",midpoint(expr,a,b,n))
print("Result obtained by simpson method: ",simpson(expr,a,b,n))
print("Exact solution: ",exact_solution(expr,a,b))
print("Error in midpoint method is: ",math.fabs(exact_solution(expr,a,b)-midpoint(expr,a,b,n)))
print("Error in simpsons method is: ",math.fabs(exact_solution(expr,a,b)-simpson(expr,a,b,n)))
print("Hello")
