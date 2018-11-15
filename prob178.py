graph = {}
for i in range(10):
	if i == 0:
		graph[0] = [1]
	elif i == 9:
		graph[i] = [8]
	else:
		graph[i] = [i-1, i+1]

print graph

