f = open("p083_matrix.txt", "r")
lines = [line.strip() for line in f.readlines()]

array = [[int(k) for k in line.split(",")] for line in lines]
length = len(array)
maxxx = 10000000000
distance = [[10000000000 for k in xrange(length)] for k in xrange(length)]

distance[0][0] = min(distance[0][0], array[0][0])

queue = []

for i in range(length):
	for j in range(length):
		queue.append([i,j])

while len(queue) > 0:
	min_val = maxxx
	coords = [] 
	for k in queue:
		if min_val > distance[k[0]][k[1]]:
			coords = k
			min_val = distance[k[0]][k[1]]

	queue.remove(coords)

	possible_cords = [[coords[0]+1, coords[1]], [coords[0]-1, coords[1]], [coords[0], coords[1]+1], [coords[0], coords[1]-1]]
	for pos in possible_cords:
		if pos in queue:
			alt = distance[coords[0]][coords[1]] + array[pos[0]][pos[1]]
			if alt < distance[pos[0]][pos[1]]:
				distance[pos[0]][pos[1]] = alt



print distance[79][79]


