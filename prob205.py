cache = {}

def ncr(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if n == r+1:
        return 1
    if r == 1:
        return 1
    if r == 2:
        if n%2 ==1:
            return (n-1)/2
        else:
            return n/2
    prob = 0
    for i in range(1,r+1):
        prob += ncr(n-r, i)
    return prob

all_cases = 4**9 * 6**6

print all_cases

prob = 0
for i in range(9,37):
    for j in range(6,i):
        # print i,j
        prob+=ncr(i,9)*ncr(j,6)

print prob

print prob*1.0/all_cases
awe = 0
for i in range(9,37):
    awe += ncr(i,9)

print awe, 4**9

print ncr(9,9), ncr(10,9), ncr(11,9)
0.00208123475926
0.00372530051874
