s = []

for i in range(1, 56):
	value = (100003 - 200003*i + 300007*i*i*i)%1000000 - 500000
	s.append(value)

for i in xrange(56, 4000001):
	value =  (s[i-25] + s[i-56] + 1000000)%1000000 - 500000
	s.append(value)


import numpy as np

nps = np.array(s)
mat = np.reshape(nps, (2000, 2000))

max_sum = 0
for i in range(2000):
	a_sum = 0
	for j in range(2000):
		a_sum += mat[i][j]
		if a_sum > max_sum:
			max_sum = a_sum

		if a_sum < 0:
			a_sum = 0


for j in range(2000):
	a_sum = 0
	for i in range(2000):
		a_sum += mat[i][j]
		if a_sum > max_sum:
			max_sum = a_sum

		if a_sum < 0:
			a_sum = 0


for j in range(2000):
	a_sum = 0
	i = 0
	now_j = j
	while now_j >= 0 and i < 2000:
		a_sum += mat[i][now_j]
		now_j -= 1
		i += 1
		if a_sum > max_sum:
			max_sum = a_sum

		if a_sum < 0:
			a_sum = 0


for i in range(2000):
	a_sum = 0
	j = 0
	now_i = i
	while now_i < 2000 and j < 2000:
		a_sum += mat[now_i][j]
		now_i += 1
		j += 1
		if a_sum > max_sum:
			max_sum = a_sum

		if a_sum < 0:
			a_sum = 0


print max_sum