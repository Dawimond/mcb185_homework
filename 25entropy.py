# 25entropy by Yutong Ji

import math
import sys

def entropy(a, c, g, t):
	tnt = a + c + g + t
	if a == 0:
		sys.exit('ERROR! Nucleotide Count Cannot be 0!')
	if c == 0:
		sys.exit('ERROR! Nucleotide Count Cannot be 0!')
	if g == 0:
		sys.exit('ERROR! Nucleotide Count Cannot be 0!')
	if t == 0:
		sys.exit('ERROR! Nucleotide Count Cannot be 0!')
	pa = a / tnt
	pc = c / tnt
	pg = g / tnt
	pt = t / tnt
	H = -(pa * math.log2(pa) + pc * math.log2(pc) + pg * math.log2(pg) + pt * math.log2(pt))
	return H

print("Example 1: Shanoon Entropy of C in AATGCCTG")
print("Entropy = ", entropy(2, 2, 2, 2))

print("Example 2: Shanoon Entropy of T in TCCCCGGGA")
print("Entropy = ", entropy(1, 4, 3, 1))

print("Example 3: Shanoon Entropy with 0 Nucleotide Count")
print("Entropy = ", entropy(0, 0, 0, 0))