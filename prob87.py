n = 10**8

fm = 50 * (10**6)

primes_list = [2]

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

print len(primes_list), primes_list[-1]

ans = set()
for i in primes_list:
	if i*i >= fm:
		break
	for j in primes_list:
		if j**3 >= fm:
			break
		for k in primes_list:
			if k**4 >= fm:
				break
			result = i*i + j**3 + k**4
			if result <= fm:
				ans.add(result)

print len(ans)
