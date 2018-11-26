def converter(n, length):
	p = [int(k) for k in list('{0:0b}'.format(n))]
	return [0]*(length - len(p)) + p

f = open("ses.txt", "r")
lines = [[int(k) for k in line.strip().split(",")] for line in f.readlines()]

# "81, 88, 75, 42, 87, 84, 86, 65" => 65 + 87 + 88 | 75 + 81 + 84
ans = 0
failed_count = 0
for line in lines:
	length = len(line)
	flag = True
	summs = []
	for i in xrange(1, 2**length):
		count = 0
		summ = 0
		for idx, nn in enumerate(converter(i, length)):
			if nn == 1:
				count+=1
				summ+=line[idx]

		summs.append(summ)

	for  i in range(2**length-1):
		if not flag:
			break
		for j in range(i+1, 2**length-1):
			ic = converter(i+1, length)
			jc = converter(j+1, length)
			sumc = [x + y for x, y in zip(ic, jc)]
			if 2 in sumc:
				continue
			else:
				if ic.count(1) > jc.count(1) and summs[i] > summs[j]:
					pass
				elif ic.count(1) < jc.count(1) and summs[i] < summs[j]:
					pass
				elif ic.count(1) == jc.count(1) and summs[i] != summs[j]:
					pass
				else:
					flag = False
					break
	if flag:
		ans += sum(line)
	else:
		failed_count += 1
		print "failed", line

print ans
print failed_count