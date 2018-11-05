n = 10**7

primes_list = [2]

i = 3
while i <= (n ** 0.5 + 1):
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

previous = 2
answer = 0
for i in xrange(3, 10**4):
  initial = i
  this_answer = 1
  while i > 1:
    for k in primes_list:
      if k > i:
        break

      count = 0
      while i%k == 0:
        if k <= i:
          i = i/k
          count = count + 1
        else:
          break
      this_answer = this_answer * (count + 1)
  print initial, this_answer, answer
  if previous == this_answer:
    answer = answer + 1
  else:
    previous = this_answer

print answer