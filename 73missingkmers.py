# 73missingkmers.py by Yutong Ji

import sys
import mcb185
import itertools

for k in range(1, 10): 
	kcnt = {}
	for deflin, seq in mcb185.read_fasta(sys.argv[1]):
		counts = 0
		for i in range(len(seq) -k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcnt:
				kcnt[kmer] = 0
			kcnt[kmer] += 1
		antiseq = mcb185.anti_seq(seq)
		for i in range(len(antiseq) -k + 1):
			kmer = antiseq[i:i+k]
			if kmer not in kcnt:
				kcnt[kmer] = 0
			kcnt[kmer] += 1
		for nts in itertools.product('ACGT', repeat = k):
			kmer = ''.join(nts)
			if kmer in kcnt: 
				continue
			else:
				print(kmer, 0)
				counts += 1
	if counts != 0:
		print('k = ' k, counts)
		break