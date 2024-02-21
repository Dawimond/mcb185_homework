# 45dndstats.py by Yutong Ji

import random

repeat = 10000
totstat3d6 = 0
totstat3d6r1 = 0
totstat3d6x2 = 0
totstat4d6d1 = 0

print('3D6:')
for rolls in range(repeat):
	stat = 0
	for rolls in range(3):
		r = random.randint(1, 6)
		stat += r
	totstat3d6 += stat
print(totstat3d6 / repeat)

print('3D6r1:')
for rolls in range(repeat):
	stat = 0
	for rolls in range(3):
		r = random.randint(1, 6)
		if r == 1: r = random.randint(1, 6)
		stat += r
	totstat3d6r1 += stat
print(totstat3d6r1 / repeat)

print('3d6x2:')
for rolls in range(repeat):
	stat = 0
	for rolls in range(3):
		r1 = random.randint(1, 6)
		r2 = random.randint(1, 6)
		if r1 > r2: stat += r1
		else:       stat += r2
	totstat3d6x2 += stat
print(totstat3d6x2 / repeat)

print('4d6d1')
for rolls in range(repeat): 
	stat = 0
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	r4 = random.randint(1, 6)
	if r1 < r2 and r1 < r3 and r1 < r4:
		stat += (r2 + r3 + r4)
	elif r2 < r1 and r2 < r3 and r2 < r4:
		stat += (r1 + r3 + r4)
	elif r3 < r1 and r3 < r2 and r3 < r4:
		stat += (r1 + r2 + r4)
	else:
		stat += (r1 + r2 + r3)
	totstat4d6d1 += stat
print(totstat4d6d1 / repeat)