import math

factorials = [1];
for i in range(1,10):
	factorials.append(factorials[-1]*i);

def sum_of_fact(i):
	answer = 0
	while i > 0:
		num = i%10
		answer= answer+factorials[num]
		num=num/10
	return answer

for i in range(1,1000000):
	li = []
