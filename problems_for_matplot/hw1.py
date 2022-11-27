import numpy as np 
import matplotlib.pyplot as plt 
import random 

ypoints = np.array([10,20,30,40,50,60,70,80,90])

yrand = random.choices(ypoints , k=25)

plt.grid()
plt.plot(yrand , marker = "^")
plt.show()
