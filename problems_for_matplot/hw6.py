import matplotlib.pyplot as plt 
import numpy as np
import math 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(-2,16,50)

x = [math.cos(i) for i in t]
y = [math.sin(i) for i in t]
z = [i for i in t]

ax.plot(x,y,z,zdir='z',marker = 'o')
ax.view_init(30,45)

plt.show()

