import matplotlib.pyplot as plt 

circle_10 = plt.Circle((0.5,0.3),0.1 , fill = False)
circle_50 = plt.Circle((0.5,0.4),0.2 , fill = False)
circle_100 = plt.Circle((0.5,0.5),0.3 , fill = False)
ax = plt.subplot()

ax.add_artist(circle_10)
ax.add_artist(circle_50)
ax.add_artist(circle_100)

plt.show()