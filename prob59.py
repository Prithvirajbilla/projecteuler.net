f = open("cipher1.txt","r")

l = f.readline()

s = [int(k) for k in l.split(",")]

# print s
for i in range(97,123):
	for j in range(97,123):
		for k in range(97,123):
			st = [i,j,k]
			hello = []
			ve = False
			for n in range(0,len(s)):
				aa = s[n] ^ st[n%3]
				if aa not in range(32,123):
					ve = True
					break
				hello+=[aa]
			if not ve:
				print ''.join(map(chr,hello))
				print sum(hello)

