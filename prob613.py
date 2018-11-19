import math

ans = 0
total_num = 0
for i in range(0, 30):
	for j in range(0, 40):
		cond = (3 * j) + (4 * i) - 120 
		if cond <= 0:
			value_num = (i*i) + (j*j) - (30*i) - (40*j)
			value_den = math.sqrt((30-i)*(30-i) + (j*j))*math.sqrt((i*i) + (40-j)*(40-j))
			value = (value_num*1.0)/value_den
			theta = math.acos(value)
			total_num +=1
			ans += theta / (2* math.pi)

print ans, round(ans/total_num, 10)

## stupid problem
## (N[Integrate[ArcTan[y/x], {x, 0, 3}, {y, 0, (4/3) x}]] + N[Integrate[ArcTan[y/x], {x, 0, 4}, {y, 0, (3/4) x}]]) /(12*Pi) + .25
## 0.3916721504087494