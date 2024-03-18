#!/usr/bin/env python3
# 91translate.py by Yutong Ji

import argparse
import dogma
import mcb185

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-m', '--min', type=int, default=100, help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='also examine the anti-parallel strand')
arg = parser.parse_args()
print('translating', arg.file, arg.min, arg.anti)

def sixfr_trans(seq, min_len):
	translated = []
	for frame in range(3):
		aas = dogma.translate((seq[frame:])).split('*')
		for aa in aas:
			if 'M' in aa:
				prot = aa[aa.find('M'):]
				if len(prot) >= min_len:
					translated.append(prot)
	return translated	

for defline, seq in mcb185.read_fasta(arg.file):
	ogstrand = sixfr_trans(seq, arg.min)
	if arg.anti:
		revcompstr = sixfr_trans(dogma.revcomp(seq), arg.min)
		for prot in revcompstr:
			ogstrand.append(prot)
	for i, prot in enumerate(ogstrand):
		print(f'>{defline[:11]}-prot-{i + 1}')
		print(f'{prot}*')