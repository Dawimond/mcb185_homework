# 37nilakantha.py by Yutong Ji

def nilakantha_pi(k, pi, sign):
	for k in range(0, 999999): 
		if k % 2 == 0: sign = 4
		else:          sign = -4
		pi = pi + (sign / ((2 * k + 3)**3 - (2 * k + 3)))
	return pi

print('pi = ', nilakantha_pi(999999, 3, 1))