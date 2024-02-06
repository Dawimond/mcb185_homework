import random

for i in range(5): 
	print(random.random())

for i in range(50): 
	print(random.choice('ACGT'), end = '')
print()

for i in range(50): 
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end = '')
	else: print(random.choice('CG'), end = '')
print()

for i in range(3): 
	print(random.randint(1, 6))

for i in range(5):
	print(random.gauss(0.0, 1.0))

z1= 0
z2 = 0
z3 = 0
limit = 100000
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)