def r2d(x):
	d = []
	for i in x:
		if (i == "M"):
			d.append(1000)
		if (i == "D"):
			d.append(500)
		if (i == "C"):
			d.append(100)
		if (i == "L"):
			d.append(50)
		if (i == "X"):
			d.append(10)
		if (i == "V"):
			d.append(5)
		if (i == "I"):
			d.append(1)
	i = 0
	sum = 0
	while (i < len(d)):
		if (i == len(d) - 1):
			sum += d[-1]
		else:
			if (d[i + 1] <= d[i]):
				sum += d[i]
			else:
				sum -= d[i]
				sum += d[i + 1]
				i += 1
		i += 1
	return sum

def d2r(x):
	x2 = str(x)
	r2 = x
	a = ""
	while (r2 > 0):
		if (r2 < 1000):
			if (int(x2[0]) < 4):
				if (len(x2) == 3):
					a = a + "C"
					r2 -= 100
				if (len(x2) == 2):
					a = a + "X"
					r2 -= 10
				if (len(x2) == 1):
					a = a + "I"
					r2 -= 1
			else:
				if (int(x2[0]) == 4):
					if (len(x2) == 3):
						a = a + "CD"
						r2 -= 400
					if (len(x2) == 2):
						a = a + "XL"
						r2 -= 40
					if (len(x2) == 1):
						a = a + "IV"
						r2 -= 4
				else:
					if (int(x2[0]) == 5 or int(x2[0]) == 6 or int(x2[0]) == 7):
						
						if (len(x2) == 3):
							a = a + "D"
							r2 -= 500
						if (len(x2) == 2):
							a = a + "L"
							r2 -= 50
						if (len(x2) == 1):
							a = a + "V"
							r2 -= 5
					else:
						if (int(x2[0]) == 9):
							if (len(x2) == 3):
								a = a + "CM"
								r2 -= 900
							if (len(x2) == 2):
								a = a + "XC"
								r2 -= 90
							if (len(x2) == 1):
								a = a + "IX"
								r2 -= 9
						else:
							if (len(x2) == 3):
								a = a + "DCCC"
								r2 -= 800
							if (len(x2) == 2):
								a = a + "LXXX"
								r2 -= 80
							if (len(x2) == 1):
								a = a + "XIII"
								r2 -= 8
		else:
			a = a + "M"
			r2 -= 1000
		print x2
		x2 = str(r2)
