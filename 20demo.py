# 20demo.py by Yutong Ji

import math
import sys

def heya():
	print('hello Mantodea :)')
# yea so basically don't use sys.exit for now unless in specific situations
def pythagoras(a, b): 
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)
x = pythagoras(3, 4)
print(x)
def neg_to_pos(n):
	assert(n < 0)
	return abs(n)
print(neg_to_pos(9))
s = 'hello world'
print(s, type(s))
a = 0.3
b = 0.1 * 3
if	 a < b: print('a < b')
elif a > b: print('a > b')
else:		print('a == b')
if math.isclose(a, b): print('close enough')