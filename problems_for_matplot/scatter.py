import matplotlib.pyplot as plt 
import numpy as np 
import random 

for i in range (0,100):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    size = random.randint(10,1000)
    plt.scatter(x,y,s = size , alpha=0.6)
plt.show()