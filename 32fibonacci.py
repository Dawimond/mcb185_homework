# 32fibonacci.py by Yutong Ji

def fibonacci(n):
	x = 0
	y = 1
	print(x)
	for n in range(n):
		prev_num = x
		x = y
		y = prev_num + y
		print(y)
		
fibonacci(9)