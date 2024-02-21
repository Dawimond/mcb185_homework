# 44randompi.py by Yutong Ji

import random
import math

in_cir = 0
total = 0

while True: 
	x = random.random()
	y = random.random()
	total += 1
	dist = math.sqrt(x**2 + y**2)
	if dist <= 1:
		in_cir += 1
	print(total, 4*in_cir / total)