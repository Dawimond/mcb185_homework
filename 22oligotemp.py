# 22oligotemp.py by Yutong Ji

import math

def small_oligo(A, T, G, C):
	return (A + T)*2 + (G + C)*4

def large_oligo(A, T, G, C):
	return 64.9 + 41*(G + C - 16.4) / (A + T + G + C)

def nt(A, T, G, C): 
	return A + T + G + C

print("Example 1: Small Oligos: A = 1, T = 1, G = 2, C = 2")
A = 1
T = 1
G = 2
C = 2
if nt(A, T, G, C) <= 13:
	print("For oligos of or smaller than 13 nt:")
	Tm = small_oligo(A, T, G, C)
	print("Tm = ", Tm)
else:
	print("For oligos longer than 13 nt:")
	Tm = large_oligo(A, T, G, C)
	print("Tm = ", Tm)

print("Example 2: Medium Oligos: A = 3, T = 3, C = 2, G = 4")
A = 3
T = 3
G = 2
C = 4
if nt(A, T, G, C) <= 13:
	print("For oligos of or smaller than 13 nt:")
	Tm = small_oligo(A, T, G, C)
	print("Tm = ", Tm)
else:
	print("For oligos longer than 13 nt:")
	Tm = large_oligo(A, T, G, C)
	print("Tm = ", Tm)
	
print("Example 3: Large Oligos: A = 5, T = 7, C = 11, G = 9")
A = 5
T = 7
G = 11
C = 9
if nt(A, T, G, C) <= 13:
	print("For oligos of or smaller than 13 nt:")
	Tm = small_oligo(A, T, G, C)
	print("Tm = ", Tm)
else:
	print("For oligos longer than 13 nt:")
	Tm = large_oligo(A, T, G, C)
	print("Tm = ", Tm)