## answer[i+1][2][0] = answer[i][2][0] answer[i][2][1] answer[i][1][0] answer[i][1][1] answer[i][0][0] answer[i][0][1]
import numpy
dp =  numpy.zeros((30,3,2))

dp[0][0][0] = 1 #o
dp[0][1][0] = 1 #a
dp[0][2][0] = 0
dp[0][0][1] = 1 #l
dp[0][1][1] = 0
dp[0][2][1] = 0

for i in range(1,30):
	for j in range(3):
		for k in range(2):
			if j == 0:
				if k == 0:
					#ooo           ooo             ooa              oaa
					dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j+1][k] +dp[i-1][j+2][k]
				else:
					#ooaaa...oool            oooo + oooao + oaao + oaal+ oaal + oool 
					dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j+1][k] +dp[i-1][j+2][k] + dp[i-1][j][k-1] + dp[i-1][j+1][k-1] +dp[i-1][j+2][k-1]

			if j == 1:
				if k == 0:
					# 00a          000a
					dp[i][j][k] = dp[i-1][j-1][k]
				else:
					# 00a          oooa
					dp[i][j][k] = dp[i-1][j-1][k]
			if j == 2:
				if k == 0:
					#0aa           
					dp[i][j][k] = dp[i-1][j-1][k]
				else:
					dp[i][j][k] = dp[i-1][j-1][k]

i = 29
ans = 0
for j in range(3):
	for k in range(2):
		print i,j,k, dp[i][j][k]
		ans += dp[i][j][k]

print ans


##