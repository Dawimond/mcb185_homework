# 53genomestats.py by Yutong Ji

import gzip
import sys
import math

def minmax(lengths):
	mini = lengths[0]
	maxi = lengths[0]
	for val in lengths:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
def mean(lengths):
	tot = 0
	for val in lengths:
		tot += val
	return tot / len(lengths)

def stddv(lengths):
	diff_sum = 0
	for val in lengths:
		diff = (val - mean(lengths)) ** 2
		diff_sum += diff
	varri = diff_sum / len(lengths)
	return math.sqrt(varri)

def median(lengths):
	lengths.sort()
	n = len(lengths)
	if n % 2 == 1:
		med = lengths[n // 2]
	else:
		num1 = lengths[n // 2 - 1]
		num2 = lengths[n // 2]
		med = (num1 + num2) / 2
	return med
	
path = sys.argv[1]
feature = sys.argv[2]

lengths = []
with gzip.open(path, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] != feature: continue
		strt = int(words[3])
		end = int(words[4])
		lengths.append(end - strt + 1)

print(len(lengths), minmax(lengths), mean(lengths), stddv(lengths), median(lengths))