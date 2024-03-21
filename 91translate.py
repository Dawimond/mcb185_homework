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

def bestprot(seq, min_len):
	longest = ''
	for frame in range(3):
		if arg.anti:
			aas = dogma.translate((seq[frame:])).split('*') + dogma.translate(mcb185.anti_seq((seq[frame:]))).split('*')
		else:
			aas = dogma.translate((seq[frame:])).split('*')	
		for aa in aas:
			if 'M' in aa:
				prot = aa[aa.find('M'):]
				if len(prot) >= min_len and len(prot) > len(longest):
					longest = prot
	return longest	

for defline, seq in mcb185.read_fasta(arg.file):
	prot = bestprot(seq, arg.min)
	print(f'>{defline}')
	print(f'{prot}*')