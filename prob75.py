limit = 15 * (10 ** 5)

num = int(limit **  (0.5))


def gcd(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 

triangles = [0]*(limit+1)
result = 0
for m in xrange(1,num+1):
	for n in xrange(1,m+1):
		if (m+n)%2 == 1 and gcd(m,n) == 1:
			a = (m*m) + (n*n)
			b = 2*m*n
			c = (m*m) - (n*n)

			p = a+b+c
			while p <= limit:
				triangles[p]+=1;
				if (triangles[p] == 1):
					result =result + 1
				if (triangles[p] == 2):
					result = result - 1
				p += a+b+c;

print result


