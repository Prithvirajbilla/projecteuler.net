import math

prime_list = [2]
n = 10**6
i = 3

while i <= int((n**0.5) + 1):
	flag = True
	for prime in prime_list:
		if i%prime == 0:
			flag = False
			break

	if flag:
		prime_list.append(i)

	i+=2



# dp[n][m] = dp[n][m-1] + dp[n-s[m]][m-1]

k = 10

cache = {}

def get_count(n, m):
	key = "%d-%d"%(n,m)
	if key in cache:
		return cache[key]
	if n == 0:
		return 1
	if m < 0:
		return 0

	if prime_list[m] > n:
		cache[key] = get_count(n, m-1)
		return cache[key]

	cache[key] = get_count(n, m-1) + get_count(n-prime_list[m], m)
	return cache[key]

max_m = len(prime_list)-1
while True:
	if k > prime_list[-1]:
		print "not found", k, prime_list[-1]
		break

	current_m = 0
	for idx, prime in enumerate(prime_list):
		if prime > k:
			current_m = idx
			break
	ans = get_count(k, current_m)
	if ans >= 5000:
		print k, ans
		break

	print k, ans
	k = k+1
