# 57birthday.py by Yutong Ji

import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matchedbd = 0

for i in range(trials):
	calendar = []
	for day in range(days):
		calendar.append(0)
	for j in range(people):
		bd = random.randint(0, days - 1)
		calendar[bd] += 1
	found_shared = False
	minmatch = 1
	for num in calendar:
		if num > 1:
			found_shared = True
	if found_shared:
		matchedbd += 1

print(matchedbd / trials)