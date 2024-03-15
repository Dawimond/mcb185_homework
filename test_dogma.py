import dogma
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(seq[336])