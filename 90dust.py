#!/usr/bin/env python3
# 90dust.py by Yutong Ji

import argparse
import math
import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

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
		seq[i] = seq[i].lower()

if arg.lower:
	for defline, seq in mcb185.read_fasta(arg.file):
		print(defline)
		masked = list(seq)
		a = seq[:arg.size].count('A')
		c = seq[:arg.size].count('C')
		g = seq[:arg.size].count('G')
		t = seq[:arg.size].count('T')
		h = entropy(a, c, g, t)
		if h < arg.entropy: 
			mask(masked, -arg.size, 0)
		for i in range(arg.size, len(seq)):
			if seq[i - arg.size] == "A": a -= 1
			if seq[i - arg.size] == "C": c -= 1
			if seq[i - arg.size] == "G": g -= 1
			else:                 t -= 1
			if seq[i] == "A":     a += 1
			if seq[i] == "C":     c += 1
			if seq[i] == "G":     g += 1
			else:                 t += 1
			h = entropy(a, c, g, t)
			if h < arg.entropy:
				mask(masked, i - arg.size, i)
		print(''.join(masked))