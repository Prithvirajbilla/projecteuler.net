def farey_function(n, descending=False):
	"""Print the nth Farey sequence, either ascending or descending."""
	a, b, c, d = 0, 1, 1, n
	if descending: 
		a, c = 1, n-1
	flag = False
	count = 0
	while (c <= n and not descending) or (a > 0 and descending):
		k = int((n + b) / d)
		a, b, c, d = c, d, (k*c-a), (k*d-b)
		if flag:
			count +=1

		if a == 1 and b == 3:
			flag = True

		if a == 1 and b == 2:
			print count
			break

farey_function(12000)