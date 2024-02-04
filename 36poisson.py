# 36poisson by Yutong Ji

import math

def poisson_prob(n, k):
	return (((n ** k) * math.e ** (-n)) / math.factorial(k))

print('Example 1: 2 events with an expectation of 0.61')
print(poisson_prob(0.61, 2))

print('Example 2: 10 events with an expectation of 0.33')
print(poisson_prob(0.33, 10))

print('Example 3: 1 events with an expectation of 1')
print(poisson_prob(1, 1))