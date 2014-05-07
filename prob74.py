import math

factorials = [1];
for i in range(1,10):
	factorials.append(factorials[-1]*i);

def sum_of_fact(i):
	answer = 0
	while i > 0:
		num = i%10
		answer= answer+factorials[num]
		i=i/10
	return answer

a = 0
for i in range(1,1000000):
	li = []
	k = i
	while k not in li:
		li.append(k)
		k = sum_of_fact(k)

	if len(li) == 60:
		a= a+1
	# print i

print a