inc_cache = {}
dec_cache = {}

def increasing_dp(last_digit, k):
	key = "%d-%d"%(last_digit, k)

	if key in inc_cache:
		return inc_cache[key]

	if last_digit == 0:
		inc_cache[key] = 0
		return 0
	if k == 1:
		inc_cache[key] = 1
		return 1
	if last_digit == 1:
		inc_cache[key] = increasing_dp(last_digit,k-1)
		return inc_cache[key]
	else:
		ans = 0
		for i in range(1, last_digit+1):
			ans += increasing_dp(i, k-1)
		inc_cache[key] = ans
		return inc_cache[key]

def decreasing_dp(last_digit, k):

	key = "%d-%d"%(last_digit, k)

	if key in dec_cache:
		return dec_cache[key]

	if k == 1:
		if last_digit == 0:
			dec_cache[key] = 0
			return dec_cache[key]
		else:
			dec_cache[key] = 1
			return 1

	if last_digit == 9:
		dec_cache[key] = decreasing_dp(last_digit,k-1)
		return dec_cache[key]
	else:
		ans = 0
		for i in range(last_digit, 10):
			ans += decreasing_dp(i, k-1)
		dec_cache[key] = ans
		return dec_cache[key]

non_bouncy_numbers = 9

for digit_count in range(2,101):
	inc = 0
	dec = 0
	for j in range(0,10):
		ansi = increasing_dp(j, digit_count)
		ansd = decreasing_dp(j, digit_count)

		# print j, digit_count, ansi, "i"
		# print j, digit_count, ansd, "d"

		inc += ansi
		dec += ansd

	inc_dec = inc + dec
	non_bouncy_numbers = non_bouncy_numbers + inc_dec - 9
	print inc, dec,inc_dec, digit_count

print non_bouncy_numbers