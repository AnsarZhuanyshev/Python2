import matplotlib.pyplot as plt 

plt.ylim(0,0.8)

circle_25 = plt.Circle((0.25,0.5),0.1 , fill = False)
circle_50 = plt.Circle((0.25,0.5),0.15 , fill = False)
circle_75 = plt.Circle((0.25,0.5),0.2 , fill = False)

circle_250 = plt.Circle((0.75,0.5),0.1 , fill = False)
circle_500 = plt.Circle((0.75,0.5),0.15 , fill = False)
circle_750 = plt.Circle((0.75,0.5),0.2 , fill = False)

ax = plt.subplot()

ax.add_artist(circle_25)
ax.add_artist(circle_50)
ax.add_artist(circle_75)
ax.add_artist(circle_250)
ax.add_artist(circle_500)
ax.add_artist(circle_750)
plt.axvline(x = 0.5 , color = "Green")
plt.show()