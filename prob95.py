n = 10**6

primes = [2]

i = 3
while i <= n:
	flag = True
	for j in primes:
		if i%j == 0:
			flag = False
			break

	if flag:
		primes.append(i)
	i = i + 2

print primes


# divisors = [0] * (10**6 + 1)

# for i in xrange(2,10**6+1):
# 	ans = 0
# 	for prime in primes:
# 		if i%prime == 0:
# 			ans += prime

# 		if i > prime:
# 			break
# 	divisors[i] = ans