import sys

def pythagoras(a, b): 
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
x = pythagoras(-3, -4)
print(x)