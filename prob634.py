# ans = set()
r = 0
n = 9 * (10**18)
i = 2
while True:
	k1 = i*i
	if k1 > n:
		break
	j = 2
	while True:
		k2 = j * j * j
		if k2 > n:
			break
		result = k1*k2
		if k1*k2 <= n:
			r = r+1
		else:
			break
		j = j +1
	i = i +1

print len(r)