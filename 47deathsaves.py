# 47deathsaves.py by Yutong Ji

import random

repeats = 10000
die = 0
stable = 0
revive = 0

for deathsave in range(repeats):
	failure = 0
	success = 0
	while True:
		roll = random.randint(1, 20)
		if roll == 1: failure += 2
		elif roll == 20: 
			revive += 1
			break
		elif roll < 10: failure += 1
		else: success += 1
		
		if failure >= 3: 
			die += 1
			break
		if success == 3:
			stable += 1
			break

diechance = die / repeats
stablechance = stable / repeats
revivechance = revive / repeats

print(f'Chance of dying: {diechance:.3f}, stabilizing: {stablechance:.3f}, reviving: {revivechance:.3f}')