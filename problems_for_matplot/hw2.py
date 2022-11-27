import matplotlib.pyplot as plt 
import numpy as np 
import random
x = np.linspace(0,2,10)
y = x 

x_scat = random.choices(x , k = 20)
y_scat = random.choices(y , k = 20)
#for i in x :
plt.plot(x , y , c = "red")
plt.scatter(x_scat , y_scat , c ="blue")
plt.show()