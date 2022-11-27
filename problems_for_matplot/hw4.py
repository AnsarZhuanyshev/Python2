import matplotlib.pyplot as plt 
import math 
import random 

values = []
percentage = []

sum = 0

for i in range (0,6):
    if sum<100:
        val = random.randint(0,15)
        values.append(val)
        sum += val
    elif sum>=100:
        val = 0
        values.append(val)
my_labels = ["Almaty","Astana","Shymkent","Atyrau","Aktobe","Kyzylorda"]

my_explode = [0.3,0,0,0,0,0]

plt.pie(values , labels=my_labels ,explode=my_explode , shadow= True)
plt.show()
