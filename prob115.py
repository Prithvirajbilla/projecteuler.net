current_n = 50

while True:
	m = 50
	dp = [ [0, 0] for i in xrange(current_n+1)]

	for i in range(1, m):
		dp[i][0] = 1
		dp[i][1] = 0

	dp[m][0] = 1
	dp[m][1] = 1

	flag = False
	for i in range(m+1,current_n+1):
		dp[i][0] = dp[i-1][0] + dp[i-1][1]
		dp[i][1] = dp[i-1][1] + dp[i-m][0]
		sum_val = dp[i][0] + dp[i][1]

		if sum_val > 10**6:
			print current_n, sum_val
			flag = True
			break
	current_n = current_n + 1
	if flag:
		break
