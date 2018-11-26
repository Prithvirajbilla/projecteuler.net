import math
def pandigital(n):
	l = str(n)
	flag = True
	for i in range(1,10):
		if str(i) not in l:
			flag = False
			break
	return flag


fib = [1, 1]
i = 2
while True:
	n = sum(fib)
	fib[i%2] = n
	i += 1

	last = n%(10**9)
	first = str(n)[:9]

	if pandigital(last):
		print i
		# break

