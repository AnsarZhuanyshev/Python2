import matplotlib.pyplot as plt 
import numpy as np 
import math 

x = np.linspace(0,5,100)
y_sin = []
y_cos = []
y_in_sin = []
y_in_cos = []
for i in x:
    val = math.sin(i)
    y_sin.append(val)
    
for j in x:
    val2 = math.cos(j)
    y_cos.append(val2)

for j in x:
    val3 = math.sin(j)
    val3 = - val3
    y_in_sin.append(val3)
    
for j in x:
    val4 = math.cos(j)
    val4 = - val4
    y_in_cos.append(val4)

plt.plot(x,y_sin,c = "Blue")
plt.plot(x,y_cos,c ="Red")
plt.plot(x,y_in_sin,c="Black")
plt.plot(x,y_in_cos,c="Green")

plt.show()