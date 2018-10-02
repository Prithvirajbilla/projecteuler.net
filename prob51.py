primes_list = [2]

i = 3
while True:
  s = i ** 0.5 + 1
  flag = True
  for x in primes_list:
    if x <= s:
      if i%x == 0:
        flag = False
        break

  if flag:
    primes_list.append(i)

  last_number = primes_list[-1]

  stringify = str(last_number)

  start_list = []
  if "0" in stringify:
    start_list.append(0)

  if "1" in stringify:
    start_list.append(1)

  if "2" in stringify:
    start_list.append(2)

  found_flag=False
  for k in start_list:
    prime_count  = 0
    new_primes = []
    for p in range(k,10):
      new_flag = True
      new_digit = int(stringify.replace(str(k), str(p)))
      s1 = new_digit ** 0.5 + 1
      for x in primes_list:
          if x <= s1:
            if new_digit%x == 0:
              new_flag = False
              break

      if new_flag:
        new_primes.append(new_digit)
        prime_count = prime_count + 1
    if prime_count == 8:
      found_flag = True
      print "Found:", i, new_primes
      break

  if found_flag:
    break

  i = i + 2


