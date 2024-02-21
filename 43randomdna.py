# 43randomdna.py by Yutong Ji

import random

totseq = 3

for i in range(totseq): 
	print(f'>seq-{i + 1}')
	for nts in range(random.randint(50, 60)): 
		print(random.choice('ACGT'), end = '')
	print()