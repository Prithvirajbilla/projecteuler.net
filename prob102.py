import math

def check_triangle(l):
	x1 = int(l[0])
	x2 = int(l[2])
	x3 = int (l[4])
	y1 = int(l[1])
	y2 = int(l[3])
	y3 = int(l[5])
	if (x1-x2)/(y1-y2)*1.0 != (x1-x3)/(y1-y3)*1.0 :
		return True
	else:
		return False

def area(x1,y1,x2,y2,x3,y3):
	return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0)

def is_inside(l):
	x=0;y=0
	x1 = int(l[0])
	x2 = int(l[2])
	x3 = int (l[4])
	y1 = int(l[1])
	y2 = int(l[3])
	y3 = int(l[5])
	A = area (x1, y1, x2, y2, x3, y3);
	A1 = area (x, y, x2, y2, x3, y3);
	A2 = area (x1, y1, x, y, x3, y3);
	A3 = area (x1, y1, x2, y2, x, y);
	if A == A1+A2+A3:
		return True
	else:
		return False
   

f = open("triangles.txt","r")

l = f.readlines()

l = [a.split(",") for a in l]

answer = 0
for i in l:
	if is_inside(i):
		answer=answer+1

print answer
