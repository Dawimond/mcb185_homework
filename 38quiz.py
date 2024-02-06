# co-authors: Roger, Natalia

def gregory_pi(k, pi, sign):
	for k in range(0, 100): 
		if k % 2 == 0: sign = 1
		else:          sign = -1
		pi = pi + (sign / (2*k + 1))
	return pi * 4

print('pi = ', gregory_pi(100, 0, 1))

def nilakantha_pi(k, pi, sign):
	for k in range(0, 100): 
		if k % 2 == 0: sign = 4
		else:          sign = -4
		pi = pi + (sign / ((2 * k + 3)**3 - (2 * k + 3)))
	return pi

print('pi = ', nilakantha_pi(100, 3, 1))