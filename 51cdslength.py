# 51cdslength.py by Yutong Ji

import gzip
import sys

lengths = []
path = sys.argv[1]
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		strt = int(words[3])
		end = int(words[4])
		lengths.append(end - strt + 1)
	print(lengths)