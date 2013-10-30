import math
l = []
for i in range(30):
	k = (i+1)*(i+2)/2
	l=l+ [k]

f = open("words.txt","r")
s = f.readline()
s = [ x[1:-1] for x in s.split(",") ]
su = 0
i = 0
for k in s:
	su= (sum(bytearray(k)) -64*(len(k)))
	if su in l:
		i = i+1

print i