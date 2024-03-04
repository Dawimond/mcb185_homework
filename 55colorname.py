# 55colorname.py by Yutong Ji

import sys
import gzip

fl = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
colinput = [R, G, B]

def dtc(P, Q):
	dis = 0
	for p, q in zip(P ,Q):
		dis += abs(p - q)
	return dis

mindis = 999
closest_color = None

with open(fl) as fp:
	for line in fp:
		words = line.split()
		name = words[0]
		code = words[2].split(',')
		rgb = (int(code[0]), int(code[1]), int(code[2]))
		d = dtc(colinput, rgb)
		if d < mindis:
			mindis = d
			closest_color = name
			
print(closest_color)