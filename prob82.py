f = open("p082_matrix.txt", "r")
lines = [line.strip() for line in f.readlines()]

array = [[int(k) for k in line.split(",")] for line in lines]

distance = [[100000 for x in range(80)] for y in range(80)]
