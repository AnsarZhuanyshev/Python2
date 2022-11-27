import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

x0 = np.array([np.random.randint(50,150) for i in range(1000)])
y0 = np.array([np.random.randint(-50,100) for i in range(1000)])
z0 = np.array([np.random.randint(-100,0) for i in range(1000)])

x1 = np.array([np.random.randint(100,200) for i in range(1000)])
y1 = np.array([np.random.randint(0,100) for i in range(1000)])
z1 = np.array([np.random.randint(-50,50) for i in range(1000)])

x2 = np.array([np.random.randint(150,250) for i in range(1000)])
y2 = np.array([np.random.randint(-50,50) for i in range(1000)])
z2 = np.array([np.random.randint(-50,0) for i in range(1000)])

ax.scatter(x0,y0,z0,color='Purple')
ax.scatter(x1,y1,z1,color='Green')
ax.scatter(x2,y2,z2,color='Yellow')

plt.show()