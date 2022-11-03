import random
import string 

list_with_letters = random.choices(string.ascii_letters, k=5)

x =''

for i in list_with_letters:
    x += i

print (x)