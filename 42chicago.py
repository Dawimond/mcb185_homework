# 42chicago.py by Yutong Ji

import random

zeroscore = 0
totalscore = 0
gamecount = 99999

for i in range(gamecount):
	score = 0
	for roundnum in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == roundnum:
			score += roundnum
	totalscore += score
	if score == 0: 
		zeroscore += 1

print(zeroscore / gamecount)
print(totalscore / gamecount)