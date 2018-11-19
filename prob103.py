def converter(n):
	p = list('{0:0b}'.format(n))
	return [0]*(7 - len(p)) + p

subset = [19, 30, 37, 38, 39, 41, 44]

tracked_sum = 248
tracked = [19, 30, 37, 38, 39, 41, 44]

diffs = [-3, -2, -1, 1, 2, 3]

for a in diffs:
	for b in diffs:
		for c in diffs:
			for d in diffs:
				for e in diffs:
					for f in diffs:
						for g in diffs:
							newly = subset[:]
							newly[0] += a
							newly[1] += b
							newly[2] += c
							newly[3] += d
							newly[4] += e
							newly[5] += f
							newly[6] += g

							flag = True
							for i in range(1,128):
								sum_0 = 0
								sum_1 = 0
								count_0 = 0
								count_1 = 0
								for idx, nn in enumerate(converter(i)):
									if nn == 0:
										count_0+=1
										sum_0+=newly[idx]
									else:
										count_1+=1
										sum_1+=newly[idx]

								if count_0 > count_1 and sum_0 > sum_1:
									pass
								elif count_0 < count_1 and sum_0 < sum_1:
									pass
								else:
									flag = False
									break

							if flag:
								new_sum = sum(newly)
								if new_sum < tracked_sum:
									tracked_sum = new_sum
									tracked = newly[:]

print tracked_sum, tracked, ''.join(str(x) for x in sorted(tracked))

## 17283537393942

## 