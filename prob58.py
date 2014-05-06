import math
actual_primes = [2]
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

side = 1
max_number = 1
primes = []
percent = 100;
while percent > 10:
	side = side+2
	n = max_number+side-1
	e = n+side-1
	w = e+side-1
	s = w+side-1
	max_number = s
	if is_prime(n):
		primes.append(n)
	if is_prime(e):
		primes.append(e)
	if is_prime(w):
		primes.append(w)
	if is_prime(s):
		primes.append(s)

	percent = len(primes)/((2*side - 1)*1.0)

	percent = percent*100
	print percent,side
print side