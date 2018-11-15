def increasing_dp(last_digit, k):
	if last_digit == 0:
		return 0
	if k == 1:
		return 1
	if last_digit == 1:
		return increasing_dp(last_digit,k-1)
	else:
		ans = 0
		for i in range(1, last_digit+1):
			ans += increasing_dp(i, k-1)
		return ans

def decreasing_dp(last_digit, k):
	if k == 1:
		if last_digit == 0:
			return 0
		else:
			return 1

	if last_digit == 9:
		return decreasing_dp(last_digit,k-1)
	else:
		ans = 0
		for i in range(last_digit, 10):
			ans += decreasing_dp(i, k-1)
		return ans

initial_count = 9
bouncy_numbers = 0

for digit_count in range(2,7):
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
	initial_count = initial_count + 10**(digit_count) - 10**(digit_count-1)
	bouncy_numbers = bouncy_numbers + 10**(digit_count) - 10**(digit_count-1) - inc_dec + 9
	print inc, dec,inc_dec,10**(digit_count) - 10**(digit_count-1), digit_count, 10**(digit_count) - 10**(digit_count-1) - inc_dec + 9, initial_count
	print (bouncy_numbers*100.0)/initial_count

initial_count = initial_count + 1
current_number = 999999+1

while True:
	list_of_ints = [int(i) for i in str(current_number)]
	inc_list = sorted(list_of_ints)
	dec_list = sorted(list_of_ints, reverse = True)
	if not (list_of_ints == inc_list or list_of_ints == dec_list):
		bouncy_numbers = bouncy_numbers + 1

	if (bouncy_numbers*100.0)/initial_count == 99:
		print current_number
		break
	initial_count = initial_count+1
	current_number = current_number + 1

