# 63dust.py by Yutong Ji

import sys
import math
import mcb185

fl = sys.argv[1]
w = int(sys.argv[2])
h = sys.argv[3]

def entropy(seq):
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	tnt = a + c + g + t
	pa = a / tnt
	pc = c / tnt
	pg = g / tnt
	pt = t / tnt
	h = -(pa * math.log2(pa) + pc * math.log2(pc) + pg * math.log2(pg) + pt * math.log2(pt))
	return h

def 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		if entropy(s) < 1.4
		