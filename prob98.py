f = open("p098_words.txt", "r")
lines = f.readlines()

words = [ word[1:-1] for word in lines[0].strip().split(",")]

word_hash = {}

for word in words:
	key = ''.join(sorted(word))

	if key not in word_hash:
		word_hash[key] = [word]
	else:
		word_hash[key].append(word)


num_hash = {}
for i in xrange(2, 10**5):
	num = i * i
	key = ''.join(sorted(str(num)))
	if key not in num_hash:
		num_hash[key] = [num]
	else:
		num_hash[key].append(num)

max_ans = 0

for key in word_hash:
	if len(word_hash[key]) > 1:
		a = word_hash[key][0]
		b =word_hash[key][1]
		p = ""
		for i in a:
			p += str(b.index(i))
		for num_key in num_hash:
			if len(num_key) == len(key) and len(num_hash[num_key]) > 1:
				for numi in num_hash[num_key]:
					for numj in num_hash[num_key]:
						pp = ""
						for numii in str(numi):
							pp += str(str(numj).index(numii))
						if pp == p:
							max_ans = max(numi, max_ans)
							max_ans = max(numj, max_ans)

print max_ans

