p = 10**8 + 10**6

def is_good(num):
	numstr = str(num)
	if len(numstr) == 17:
		flag = True
		for i in range(0,18,2):
			if numstr[i] != str(i/2+1):
				return False
		return flag
	return False

i = 1
vals = [3,7]
while True:
	flag = False
	for k in vals:
		p1 = p + (10*i) + k
		if p1 > 10**17:
			flag = True
			break

		if is_good(p1*p1):
			print p1*p1
			flag = True
			break
	if flag:
		break
	i = i + 1

print is_good("1_2_3_4_5_6_7_8_9")