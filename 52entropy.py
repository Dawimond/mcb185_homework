# 52entropy.py by Yutong Ji

import sys
import math

probs = []
for arg in sys.argv[1:]:
	f = float(arg)
	if f <= 0 or f >= 1: sys.exit('ERROR! Not a Probability')
	probs.append(float(arg))
total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
	sys.exit('ERROR! Probability Sum Must be 1.0')
h = 0
for p in probs:
	h -= p * math.log2(p)

print(h)