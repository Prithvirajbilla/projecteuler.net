import numpy as np

f = open("p096_sudoku.txt", "r")
lines = [line.strip() for line in f.readlines()]

sudokus = np.reshape(lines, (-1, 10))

def solve(grid):
	flag = True
	for i in range(9):
		for j in range(9):
			if grid[i][j] == 0:
				# print i,j, grid[i][j],grid
				flag = False
				all_numbers = set(range(1,10))
				for ki in range(9):
					if grid[ki][j] in all_numbers:
						all_numbers.remove(grid[ki][j])

				for kj in range(9):
					if grid[i][kj] in all_numbers:
						all_numbers.remove(grid[i][kj])

				square_x = (i//3)*3
				square_y = (j//3)*3
				for ki in range(square_x, square_x + 3):
					for kj in range(square_y, square_y + 3):
						if grid[ki][kj] in all_numbers:
							all_numbers.remove(grid[ki][kj])


				possible_ones = list(all_numbers)

				for possible in possible_ones:
					grid[i][j] = possible
					ans = solve(grid)
					if ans:
						return ans
					grid[i][j] = 0


	if flag:
		return sum(grid[0][:3])

def grid_(sudoku):
	_grid = [[int(k) for k in row] for row in sudoku]
	return _grid


def findNextCellToFill(grid, i, j):
		for x in range(i,9):
				for y in range(j,9):
						if grid[x][y] == 0:
								return x,y
		for x in range(0,9):
				for y in range(0,9):
						if grid[x][y] == 0:
								return x,y
		return -1,-1

def isValid(grid, i, j, e):
		rowOk = all([e != grid[i][x] for x in range(9)])
		if rowOk:
				columnOk = all([e != grid[x][j] for x in range(9)])
				if columnOk:
						# finding the top left x,y co-ordinates of the section containing the i,j cell
						secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
						for x in range(secTopX, secTopX+3):
								for y in range(secTopY, secTopY+3):
										if grid[x][y] == e:
												return False
						return True
		return False

def solveSudoku(grid, i=0, j=0):
		i,j = findNextCellToFill(grid, i, j)
		if i == -1:
				return True
		for e in range(1,10):
				if isValid(grid,i,j,e):
						grid[i][j] = e
						if solveSudoku(grid, i, j):
								return True
						# Undo the current cell for backtracking
						grid[i][j] = 0
		return False

ans = 0
for sudoku in sudokus:
	g = grid_(sudoku[1:])
	solveSudoku(g)
	ans += g[0][0] * 100 + g[0][1] * 10 + g[0][2]

print ans
