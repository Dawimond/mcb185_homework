# 62skewer.py by Yutong Ji

import sys
import mcb185


fl = sys.argv[1]
w = int(sys.argv[2])

def count_gc_in_w(seq, w):
    g = seq[:w].count('G')
    c = seq[:w].count('C')
    for i in range(w, len(seq)):
        if seq[i - w] == 'G':
            g -= 1
        elif seq[i - w] == 'C':
        	c -= 1
        if seq[i] == 'G':
            g += 1
        elif seq[i] == 'C':
        	c += 1
        print(f'{(g + c)/(w):.3f}, {(g - c) / (g + c):.3f}')

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(count_gc_in_w(seq, w))