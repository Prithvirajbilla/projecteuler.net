n = 10**8

def primes(ubound):
    size = (ubound - 3) / 2
    a = [False] * size
    s = 0
    primes = []
    while s < size:
        t = 2 * s
        p = t + 3
        primes.append(p)
        for n in range(t * (s + 3) + 3, size, p):
            a[n] = True
        s = s + 1
        while s < size and a[s]:
            s = s + 1
    return primes

primes_list = primes(100000000)


print len(primes_list), primes_list[-1]

prime_set = set(primes_list)
i = 1
sum_ans = 1
while True:
  required_num = 4 * i - 2
  if required_num > n:
    break

  if required_num+1 in prime_set:
    if (required_num/2) + 2 in prime_set:
      flag = True
      for divisor in xrange(2, required_num):
        if divisor*divisor > required_num:
          break

        if required_num%divisor == 0:
          if required_num/divisor + divisor not in prime_set:
            flag = False
            break
      if flag:
        print required_num
        sum_ans += required_num

  i = i + 1


print sum_ans