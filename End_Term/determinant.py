import re

quadratic_equation_matcher = re.compile(r'(-?\d+)\*x\**2\([+-]\d+)\*x\([+-]\d+)')
quadratic_equation = '-x**3+8*x**2+15*x+5'
matches = quadratic_equation_matcher.match(quadratic_equation)

print (matches.group(1))
print(matches.group(2))
print(matches.group(3))