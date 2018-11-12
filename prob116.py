dp_cache = {}

def dp(number_of_tiles, length, length_of_tile):
	key = "%d-%d"%(number_of_tiles, length)
	if key in dp_cache:
		return dp_cache[key]

	if number_of_tiles == 1:
		ans= length - length_of_tile + 1
		if ans > 0:
			dp_cache[key] = ans
			return ans
		else:
			dp_cache[key] = 0
			return 0
	else:
		ans = 0
		r = length - length_of_tile
		if r > 0:
			for i in range(r+1):
				res = dp(number_of_tiles-1,i, length_of_tile)
				# print number_of_tiles-1,i, length_of_tile, res
				ans += res
			dp_cache[key] = ans
			return ans
		else:
			dp_cache[key] = 0
			return 0
anss = 0
for i in range(1,30):
	res = dp(i, 50, 2)
	anss += res

print anss
