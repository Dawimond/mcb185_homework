# 74genefinder.py by Yutong Ji

import sys
import mcb185

min_length = int(sys.argv[2])		

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	revseq = mcb185.anti_seq(seq)
	start_cdn = 'ATG'
	end_cdn = ['TAA', 'TAG', 'TGA']
	for frame in range(3):
		for i in range(frame, len(seq), 3):
			if seq[i:i+3] == start_cdn:
				start_idx = i
				for j in range(i + 3, len(seq), 3):
					if seq[j:j+3] in end_cdn:
						end_idx = j + 2
						if end_idx - start_idx >= min_length:
							print(start_idx, end_idx)
						break