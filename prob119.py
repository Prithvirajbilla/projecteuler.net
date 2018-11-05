def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def count_digits(n):
    s = 0
    while n:
        s+=1
        n //= 10
    return s

# i = 10
# c = 0
# while c <= 30:
# 	s = sum_digits(i)
# 	flag = False
# 	now_i = i
# 	while now_i%s == 0 and s != 1:
# 		now_i = now_i/s

# 	if now_i == 1:
# 		flag = True

# 	if flag:
# 		print c,i,s
# 		c = c + 1

# 	i = i +1

def final_digit(n,i):
    p = n*i
    return p%10

i = 9
ans = []
while i < 100:
    if len(ans) == 60:
        break

    initial = i
    count = 0
    while count < 20:
        if sum_digits(initial) == i:
            ans.append(initial)
        initial = initial * i
        count = count + 1
    i = i + 1

print sorted(ans), ans[29]