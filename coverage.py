# i dont understand needs review

import sys
import random

csize = int(sys.argv[1])
rsize = int(sys.argv[2])
rnum = int(sys.argv[3])

# setup empty chrom
chrom = []
for i in range(csize):
	chrom.append(0)
	
# fill w reads
for i in range(rnum): 
	pos = random.randint(0, csize-rsize)
	for j in range(rsize):
		chrom[pos + j] += 1
print(chrom)

# min coverage
min = rnum
for n in chrom[rsize:-rsize]:
	if n < min: 
		min = n
print(min)

# window
k = 3
seq = 'ATCGTAGTGCTATGCTAGTGCGATCC'
for i in range(0, len(seq) - k + 1, 1):  # skips per k(3) cuz codons
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	print(i, win, (g + c) / k)