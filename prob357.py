n = 10**8
under = 10**8

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


print len(primes_list), primes_list[-1]

for i in range(100):
  divsors = []
  for j in range(1, i+1):
    if i%j == 0:
      divsors.append(j)
  flag = True
  for div in divsors:
    if (div + (i/div)) not in primes_list:
      flag = False
      break
  if flag:
    print i, divsors