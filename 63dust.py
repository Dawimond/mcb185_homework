# 63dust.py by Yutong Ji

import sys
import math
import mcb185

w = int(sys.argv[2])
h_lim = float(sys.argv[3])

def entropy(a, c, g, t):
	non_zero = []
	for ct in [a, c, g, t]:
		if ct > 0: non_zero.append(ct)
	tnt = 0
	for ct in non_zero:
		tnt += ct
	probs = []
	for ct in non_zero: probs.append(ct / tnt)
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h

def mask(seq, beg, end):
	for i in range(beg, end):
		seq[i] = 'N'

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	masked = list(seq)
	a = seq[:w].count('A')
	c = seq[:w].count('C')
	g = seq[:w].count('G')
	t = seq[:w].count('T')
	h = entropy(a, c, g, t)
	if h < h_lim: 
		mask(masked, 0, w)
	for i in range(w, len(seq)):
		if seq[i - w] == "A": a -= 1
		elif seq[i - w] == "C": c -= 1
		elif seq[i - w] == "G": g -= 1
		else:                 t -= 1
		if seq[i] == "A":     a += 1
		elif seq[i] == "C":     c += 1
		elif seq[i] == "G":     g += 1
		else:                 t += 1
		h = entropy(a, c, g, t)
		if h < h_lim:
			mask(masked, i - w + 1, i + 1)
	print(''.join(masked))