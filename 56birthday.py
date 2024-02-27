# 56birthday.py by Yutong Ji

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matchedbd = 0
for i in range(trials): 
	# random bd
	bds = []
	for j in range(people):
		bd = random.randint(1, days)
		bds.append(bd)
		
	# check for collisions
	found_shared = False
	for k in range(len(bds)):
		for l in range(k + 1, len(bds)):
			if bds[k] == bds[l]:
				found_shared = True
				
	# add counts
	if found_shared:
		matchedbd += 1
		
print(matchedbd / trials)