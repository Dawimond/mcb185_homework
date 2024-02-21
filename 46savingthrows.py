# 46savingthrows.py by Yutong Ji

import random

repeat = 10000
print('DC  Norm   Adv   Dis')
for dc in range(5, 16, 5):
	norm = 0
	adv = 0
	dis = 0
	for i in range(repeat):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= dc:
			norm += 1
		if r1 >= dc and r2 >= dc:
			dis += 1
		if r1 >= dc or r2 >= dc: 
			adv += 1
	print(dc, norm / repeat, adv / repeat, dis / repeat)