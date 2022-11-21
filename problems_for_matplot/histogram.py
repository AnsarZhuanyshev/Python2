import matplotlib.pyplot as plt
import random 

x = ["Monday" , "Tueday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
y = []
z = ["Black" , "Green" , "Yellow" , "Blue" , "Red" , "Purple" , "Orange"]
for i in range(0,7):
    num = random.randint(0,100)
    y.append(num)

plt.bar(x,y,color = z , alpha = 0.5)
plt.show()