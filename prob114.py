dp = [ [0, 0] for i in range(53)]

dp[1][0] = 1
dp[1][1] = 0
dp[2][0] = 1
dp[2][1] = 0
dp[3][0] = 1
dp[3][1] = 1

for i in range(4,51):
	print i
	dp[i][0] = dp[i-1][0] + dp[i-1][1]
	dp[i][1] = dp[i-1][1] + dp[i-3][0]
	print dp[i][0], dp[i][1]

print dp[7][0], dp[7][1], dp[50][0] + dp[50][1]
