# 70demo.py by Yutong Ji

d = {}
d = dict()
d = {'dog': 'woof', 'cat': 'meow'}
print(d['cat'])
d['pig'] = 'oink'
d['cat'] = 'mew'
print(d)
# del d['cat']
if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')
for k, v in d.items(): print(k, 'says', v)
for thing in d.items(): print(thing[0], thing[1])
print(d.keys(), d.values(), list(d.values()))
# best way
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)

count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
    
# Sorting
for k in sorted(count): print(k, count[k])
#Sort by value
#for k, v in sorted(count.items(), key=lambda item: item[1]):
#	print(k, v)
#def by_value(tuple):
#	return tuple[1]
#for k, v in sorted(count.items(), key=by_value):
#	print(k, v)