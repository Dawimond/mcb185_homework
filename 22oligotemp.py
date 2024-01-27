# 22oligotemp.py by Yutong Ji

import math

def oligo(a, c, g, t):
	if  a + c + g + t <= 13: 
		Tm = (a + t) * 2 + (g + c) * 4
	else: 
		Tm = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
	return Tm

print("Example 1: Small Oligos: A = 1, T = 1, G = 2, C = 2")
print("Tm = ", oligo(1, 1, 2, 2))

print("Example 2: Medium Oligos: A = 3, T = 3, C = 2, G = 4")
print("Tm = ", oligo(3, 3, 2, 4))

print("Example 3: Large Oligos: A = 5, T = 7, C = 11, G = 9")
print("Tm = ", oligo(5, 7, 11, 9))