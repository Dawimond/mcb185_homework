# 41zscores.py by Yutong Ji

import random

z1 = 0
z2 = 0
z3 = 0
sample_size = 100000
for i in range(sample_size):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1

print(1 - 2*z1/sample_size)
print(1 - 2*z2/sample_size)
print(1 - 2*z3/sample_size)