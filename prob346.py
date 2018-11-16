n = 10**12
repunits = {}

base = 2
while True:
	i = 1
	current_sum = 1	
	while True:
		current_sum += (base**i)
		if current_sum in repunits:
			repunits[current_sum] = repunits[current_sum] + 1
		else:
			if current_sum > (n**0.5) and current_sum < n:
				repunits[current_sum] = 2
			else:
				repunits[current_sum] = 1
		if current_sum > n:
			break
		i = i + 1
	base = base + 1
	if (base) + (base*base) + 1 > n:
		break

summ = 0
for key, value in repunits.items():
	if value > 1:
		summ += key
		# print key

print summ
