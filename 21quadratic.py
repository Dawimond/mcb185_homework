# 21quadratic.py by Yutong Ji

import math
import sys

def no_more_quad(a, b, c):
	if  b**2 - 4*a*c < 0: 
		sys.exit('ERROR! Negative Discriminant!')
	x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
	x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
	return x1, x2

print("Example 1: a = 2, b = 7, c = -9")
print("x1, x2 = ", no_more_quad(2, 7, -9))

print("Example 2: a = 1, b = 8, c = 5")
print("x1, x2 = ", no_more_quad(1, 8, 5))

print("Example 3: a = 24, b = 1, c = 3")
print("x1, x2 = ", no_more_quad(24, 1, 3))