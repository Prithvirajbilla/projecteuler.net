
def rep_digits(n):
    s = [0]*10
    while n:
        s[n % 10] = s[n % 10] + 1
        n //= 10
    return s

i = 1
hash_dict = {}

while True:
	num = i * i * i
	rep = "-".join([str(x) for x in rep_digits(num)])
	if rep in hash_dict:
		hash_dict[rep].append(i)
		if len(hash_dict[rep]) == 5:
			print hash_dict[rep]
			break
	else:
		hash_dict[rep] = [i]
	i = i  + 1


