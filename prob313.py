n = 10**2
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

possible_answers = []
prime_sq = 0
for k in primes_list:
  if k >= under:
    break

  if ((k*k) + 11)%4 == 0:
    print k, ((k*k)+11)/4
    possible_answers.append(((k*k)+11)/4)

print prime_sq
print "len", len(possible_answers)

ans = 0
for k in possible_answers:
  print k
  ans += (k-3)

print ans