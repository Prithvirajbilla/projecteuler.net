import math

f = open("names.txt","r")
s = f.readline()
s = [ x[1:-1] for x in s.split(",") ]
su = 0
i = 1
for k in sorted(set(s)):
	su= su+(sum(bytearray(k)) -64*(len(k)))*i
	i = i+1

print su