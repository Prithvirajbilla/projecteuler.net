hash_dict = {}

def ncr(n, r):
	if n == 0 or r == 0:
		hash_dict["%d-%d"%(n,r)] = 1
		return 1
	if n == r:
		hash_dict["%d-%d"%(n,r)] = 1
		return 1
	# ncr = n-1cr + n-1cr-1
	hash_dict["%d-%d"%(n,r)]= hash_dict["%d-%d"%(n-1,r)] + hash_dict["%d-%d"%(n-1,r-1)]

	return hash_dict["%d-%d"%(n,r)]

ncrs = set()
for i in xrange(0,51):
	for j in xrange(0,i+1):
		ncrs.add(ncr(i,j))

ncrs = sorted(ncrs)

n = 1000000000000

print len(ncrs), ncrs[-1]

primes_list = [2]
## 126410606437752
i = 3
while i <= (n ** 0.5 + 1):
  s = i ** 0.5 + 1
  flag = True
  for x in primes_list:
    if x <= s:
      if i%x == 0:
        flag = False
        break

  if flag:
    primes_list.append(i)

  i = i + 2

answer = 0
for ncr_value in ncrs:
	flag = True
	flag_num = 0
	for prime in primes_list:
		prime_square = prime * prime
		if prime_square > ncr_value:
			break

		if ncr_value % prime_square == 0:
			flag_num = prime_square
			flag = False
			break

	if flag:
		if ncr_value > primes_list[-1] * primes_list[-1]:
			if flag_num == 0:
				print ncr_value, n
		answer = answer + ncr_value

print answer



"""
1210759611137226
"""
