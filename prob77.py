# https://en.wikipedia.org/wiki/Farey_sequence
last = []
min_val = 1
for b in xrange(1, 1000001):
	a_part = 3*b - 1
	if a_part%7 == 0:
		a = a_part/7
		current_diff = 1.0/(7*b)
		if current_diff < min_val:
			last = [a, b]
			min_val = current_diff

print last, current_diff