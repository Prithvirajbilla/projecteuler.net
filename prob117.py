dp_cache = {}
length_of_tiles = [2,3,4]
def dp(number_of_tiles, length):
	key = "%d-%d-%d-%d"%(number_of_tiles[0],number_of_tiles[1], number_of_tiles[2], length)
	if key in dp_cache:
		return dp_cache[key]

	final_ans = 0
	for idx, no in enumerate(number_of_tiles):
		if no == 1:
			ans= length - length_of_tiles[idx] + 1
			if ans > 0:
				final_ans = final_ans + ans
		else:
			r = length - length_of_tiles[idx]
			ans = 0
			if r > 0:
				for i in range(r+1):
					copied_array = [number_of_tiles[0], number_of_tiles[1], number_of_tiles[2]]
					copied_array[idx] = copied_array[idx] - 1
					res = dp(copied_array, i)
					ans += res
				final_ans = final_ans + ans
			else:
				dp_cache[key] = 0
	dp_cache[key] = final_ans
	return final_ans

result = 0
for i in range(1, 3):
	for j in range(1, 3):
		for k in range(1, 3):
			partial_ans = dp([i,j,k], 5)
			print i, j, k, partial_ans
			result  = result +  partial_ans

print result