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

for i in range(len(my_labels)):
    perc = "For "+my_labels[i]+" is "+str(values[i])+"%"
    percentage.append(perc)

plt.pie(values , labels=my_labels , shadow= True)
plt.legend(percentage)
plt.show()