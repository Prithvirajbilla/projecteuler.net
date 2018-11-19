n = 10**9
under = 100

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
