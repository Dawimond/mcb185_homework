# 21quadratic.py by Yutong Ji

import math
import sys

def no_more_quad(a, b, c):
	assert(b**2 - 4*a*c >= 0)
	if b**2 - 4*a*c < 0: sys.exit("ERROR! Negative Discriminant!")
	x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
	x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
	return x1, x2

print("Example 1: a = 2, b = 7, c = -9")
a = 2
b = 7
c = -9
if(b**2 - (4*a*c) < 0):
	print("ERROR! Negative Discriminant!")
elif(a == 0):
	print("ERROR! Denominator Cannot be 0!")
else:
	print("x1, x2 = ", no_more_quad(a,b,c))

print("Example 2: a = 24, b = 4, c = 3")
a = 24
b = 4
c = 3
if(b**2 - (4*a*c) < 0):
	print("ERROR! Negative Discriminant!")
elif(a == 0):
	print("ERROR! Denominator Cannot be 0!")
else:
	print("x1, x2 = ", no_more_quad(a,b,c))
	
print("Example 3: a = 0, b = 0, c = 0")
a = 0
b = 1
c = 1
if(b**2 - (4*a*c) < 0):
	print("ERROR! Negative Discriminant!")
elif(a == 0):
	print("ERROR! Denominator Cannot be 0!")
else:
	print("x1, x2 = ", no_more_quad(a,b,c))