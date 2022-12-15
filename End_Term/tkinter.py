import re 

s ='  x**2 - 3*x + 1'

print('Remove all spaces using regex:\n', re.sub(r"\s+", "", s), sep='')