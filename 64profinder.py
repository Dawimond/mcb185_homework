# 64profinder.py by Yutong Ji

import sys
import mcb185
import dogma

min_length = int(sys.argv[2])

def sixfr_trans(seq, min_length):
	translated = []
	for frame in range(3):
		aas = dogma.translate((seq[frame:])).split('*')
		for aa in aas:
			if 'M' in aa:
				prot = aa[aa.find('M'):]
				if len(prot) >= min_length:
					translated.append(prot)
	return translated	

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	ogstrand = sixfr_trans(seq, min_length)
	revcompstr = sixfr_trans(dogma.revcomp(seq), min_length)
	for prot in revcompstr:
		ogstrand.append(prot)
	for i, prot in enumerate(ogstrand):
		print(f'>{defline[:11]}-prot-{i}')
		print(f'{prot}*')