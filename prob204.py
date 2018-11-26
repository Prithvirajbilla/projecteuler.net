n = 100

primes_list = [2]

i = 3
while i <= n:
  s = i ** 0.5 + 1
  flag = True
  for x in primes_list:
    if x <= s:
      if i%x == 0:
        flag = False
        break

  if flag:
    primes_list.append(i)

  i = i + 2

print primes_list, len(primes_list)

large= 10**9
hash_dict = {}
final_sum = 1
for i in primes_list:
  j = 1
  hash_dict[i] = [1]
  while True:
    value = hash_dict[i][-1] * i
    if value > large:
      break
    hash_dict[i].append(value)
  final_sum = final_sum*(len(hash_dict[i])-1)
  print i, len(hash_dict[i])

print final_sum

#54311465779200000000