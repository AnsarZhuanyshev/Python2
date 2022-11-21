import matplotlib.pyplot as plt 
import random

plt.subplot(221)
plt.title("Spring")
for i in range (0,100):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    plt.scatter(x,y,s = 10 , c = "Green")


plt.subplot(222)
plt.title("Summer")
for i in range (0,100):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    plt.scatter(x,y,s = 10 , c = "Yellow")


plt.subplot(223)
plt.title("Autumn")
for i in range (0,100):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    plt.scatter(x,y,s =10 , c = "Red")


plt.subplot(224)
plt.title("Winter")
for i in range (0,100):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    plt.scatter(x,y,s =10 , c = "Blue")
plt.show()