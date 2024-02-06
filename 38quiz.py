# By Yutong Ji, co-authors: Roger, Natalia

pi = 1
sign = -1
for n in range(1, 101, 2): 
	pi = pi + (sign * (1/(n + 2)))
	print(n, sign, 4*pi)
	sign = -sign

pi_n = 3
for k in range(0, 101): 
	if k % 2 == 0: sign_n = 4
	else:          sign_n = -4
	pi_n = pi_n + (sign_n / ((2 * k + 3)**3 - (2 * k + 3)))