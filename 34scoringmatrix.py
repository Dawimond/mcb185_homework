# 34scoringmatrix.py by Yutong Ji

nts = 'ACGT'

print('   A  C  G  T')
for nt1 in nts: 
	print(nt1, end = ' ')
	for nt2 in nts: 
		if nt1 == nt2: 
			print('+1', end = ' ')
		else:
			print('-1', end = ' ')
	print()