# 35nchoosek.py by Yutong Ji

import math

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	return factorial(n) // (factorial(n-k) * factorial(k))

print('Example 1: 25 choose 5')
print(nchoosek(25, 5))

print('Example 2: 100 choose 77')
print(nchoosek(100, 77))

print('Example 1: 1 choose 1')
print(nchoosek(1, 1))