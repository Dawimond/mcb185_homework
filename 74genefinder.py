# 74genefinder.py by Yutong Ji

import sys
import mcb185

min_length = int(sys.argv[2])		

def gene_finder(seq):
	coords = {}
	start_cdn = 'ATG'
	stop_cdn = ['TAA', 'TAG', 'TGA']
	for frame in range(3):
		i = frame
		while i < len(seq):
			if seq[i:i+3] == start_cdn:
				start_idx = i
				for j in range(i + 3, len(seq), 3):
					if seq[j:j+3] in stop_cdn:
						stop_idx = j
						if stop_idx - start_idx >= min_length:
							coords[start_idx] = stop_idx + 2
							i = stop_idx
						break
			i += 3
	return coords

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	coordinations = gene_finder(seq)
	for k, v in coordinations.items():
		print(k, v)
	for k, v in coordinations.items():
		k = len(seq) - k - 1
		v = len(seq) - v - 1
		print(k, v)