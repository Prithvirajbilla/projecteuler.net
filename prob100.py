import math

i = 10**6
max_n = 10**12
a = [1,3]
while True:
	new_a = 6*a[-1] - a[-2] - 2
	a.append(new_a)
	_srt = 8*new_a*new_a -8 * new_a + 1
	n = (1+math.sqrt(_srt))/2
	print str(n), a[-1]
	if n > max_n:
		print str(n), a[-1]
		break
	# print i
	# 1235216565974041
	# 1342284446191393385645665
	# 7823407075306835066166435
	1163158972382034742453