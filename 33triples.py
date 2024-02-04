# 33triples.py by Yutong Ji

import math

for a in range(1, 100):
	for b in range(a + 1, 100):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0 and c < (a + b):
			print(a, b, c)